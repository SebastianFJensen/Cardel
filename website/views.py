from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from .models import Record , Comment , RecordResource
from .forms import AddRecordForms , CommentForm, ImportRecordDataForm
from django.views.generic.edit import CreateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .resources import RecordResource
from django.contrib.auth.decorators import login_required
from tablib import Dataset
import pandas as pd
from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from import_export.formats.base_formats import CSV , XLS , XLSX
from import_export import resources
from django.views.generic import View
from openpyxl import load_workbook
from .filters import RecordFilter



def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Du er logget ind")
    records = Record.objects.all()
    return render(request, 'home.html', {'records': records})

def login_user (request): 
	pass

def logout_user (request):
	logout(request)
	messages.success(request, "Du er nu logget ud")
	return redirect('home')

def customer_record(request, pk):
	if request.user.is_authenticated:
		customer_record = Record.objects.get(id=pk)
		if request.method == "POST":
			messages.success(request, "Sagen er blevet gemt")
			return redirect('Record')
		else:
			return render(request, "Record.html", {'customer_record':customer_record})

	
	else: 
			messages.success(request, "Du skal være logget ind for at se siden")
			return redirect('home')

	myFilter = RecordFilter


def delete_record (request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Registrering er slettet")
		return redirect('home')

	else:
			messages.success(request, "Du skal være logget ind for at se siden")
			return redirect('home')


def add_record(request):
	form = AddRecordForms(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Registrering er tilføjet...")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "Du skal være logget ind for at se siden")
		return redirect('home')

def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForms(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Sagen er blevet opdateret")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "Du skal være logget ind for at se siden")
		return redirect('home')


class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm 
	template_name = 'add_comment.html'

	def form_valid(self, form):
			form.instance.post_id = self.kwargs['pk']
			return super().form_valid(form)
	success_url = reverse_lazy('home')

class ImportRecordData(View):
    form_class = ImportRecordDataForm
    template_name = 'importrecorddata.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # import record data logic goes here
            # ...
            return redirect('home')
        return render(request, self.template_name, {'form': form})


def import_from_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES['excel_file']
        wb = load_workbook(excel_file)
        ws = wb.active

        for row in ws.iter_rows(min_row=2, values_only=True):
            created_at, BFE_Nummer, Adresse, Kommune, Region, Kontaktperson, Mail, Telefonnummer, m2, Kommuneplan, Lokalplan, Formål = row
            customer_record.objects.create(created_at=created_at, BFE_Nummer=BFE_Nummer, Adresse=Adresse, Kommune=Kommune, Region=Region, Kontaktperson=Kontaktperson, Mail=Mail, Telefonnummer=Telefonnummer, m2=m2, Kommuneplan=Kommuneplan, Lokalplan=Lokalplan, Formål=Formål)

        return render(request, 'import_success.html')

    return render(request, 'import_form.html')

@login_required
def folder(request,folderid=1):
    
    folder = get_object_or_404(Folder,id=folderid)
    files = File.objects.filter(folder=folder)
    if request.method == 'POST':
        file = request.FILES.get('uploadfile')
        filename = request.POST.get('filename')
        if file and filename:
            File.objects.create(filename=filename,file=file,folder=folder)
            return redirect(reverse('website:folder',kwargs={'folderid':folderid}))
    context = {
        'folder':folder,
        'files':files
    }
    return render(request,'website/folder.html',context)

@login_required
def deleteFolder(request,folderid):
    folder = get_object_or_404(Folder,id=folderid)
    folder.delete()
    messages.success(request,'Deleted successfully')
    return redirect('home')

@login_required
def addFolder(request):
    if request.method == 'POST':
        folder_name = request.POST.get('addfolder')
        description = request.POST.get('description')
        folder = Folder.objects.create(foldername=folder_name,folderuser=request.user,description=description)
        if folder:
            return redirect('home')
        else:
            messages.warning(request,'Folder is not created!')
            return redirect('home')

#def sendt_til_dla(request, pk)
	#customer_record = customer_record.objects.get(id=pk)
	#customer_record.sendt_til_dla == True if request.GET.get('Sendt_til_DLA') == 'True' else False
	#customer_record.save()

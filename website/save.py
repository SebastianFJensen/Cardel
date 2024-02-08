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

@receiver(post_save, sender=Record)
def create_folder(sender, instance=None, created=False, **kwargs):
    if created:
        foldername = instance.BFE_Nummer
        folder_path = os.path.join('media', 'folders', foldername)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        subfolder_names = ["Aftaler", "Økonomi", "Planer", "Bilag"]
        for subfolder_name in subfolder_names:
            subfolder_path = os.path.join(folder_path, subfolder_name)
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)
        return folder_path

        
class Folder(MPTTModel):
    parent = TreeForeignKey('self', related_name='children', null=True,
                            blank=True, db_index=True,
                            on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    creator = models.ForeignKey(Record, on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

def upload_file(request):
    uploaded_files = request.FILES.getlist('uploadfile')
    folder_id = request.POST.get('fid')
    folder = get_object_or_404(Folder, pk=folder_id)
    file = File.objects.create(folder=folder)
    for file in uploaded_files:
        FileItem.objects.create(file_field=file)

    return redirect('open_folder', pk=folder_id)

class File(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, related_name='allfiles')

    def __str__(self):
        return f"{self.pk}"

class FileItem(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='file_items')
    file_field = models.FileField(upload_to=get_file_location)

    def __str__(self):
        return f"{self.file_field}"


class Upload_fileView(View):
    def upload_file(request):
        uploaded_file = request.FILES.get('uploadfile')
        folder_id = request.POST.get('fid')
        folder = get_object_or_404(Folder, pk=folder_id)
        File.objects.create(folder=folder, files=uploaded_file)

    def get_success_url(self):
        return reverse_lazy('Record', kwargs={'pk': self.kwargs['pk']})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
        
class CustomerRecordView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            customer_record = Record.objects.get(id=pk)
            folders = customer_record.folders.all()
            form = CommentForm()
            return render(request, "Record.html", {'customer_record':customer_record, 'folders':folders, 'form':form})
        else:
            messages.success(request, "Du skal være logget ind for at se siden")
            return redirect('home')

    def post(self, request, pk):
        if request.user.is_authenticated:
            customer_record = Record.objects.get(id=pk)
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post_id = customer_record
                comment.user = request.user
                comment.save()
                messages.success(request, "Sagen er blevet gemt")
                return redirect('Record', pk=pk)
            else:
                messages.success(request, "Der opstod en fejl")
                return redirect('Record', pk=pk)
        else:
            messages.success(request, "Du skal være logget ind for at se siden")
            return redirect('home')
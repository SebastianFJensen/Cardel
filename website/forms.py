from django import forms
from django.contrib.auth.models import User
from .models import Record, Comment

class AddRecordForms(forms.ModelForm):
	BFE_Nummer = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"BFE Nummer", "class":"form-control"}), label="")
	Adresse = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Adresse", "class":"form-control"}), label="")
	Kommune = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Kommune", "class":"form-control"}), label="")
	Region = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Region", "class":"form-control"}), label="")
	Kontaktperson = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Kontaktperson", "class":"form-control"}), label="")
	Mail = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Mail", "class":"form-control"}), label="")
	Telefonnummer = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Telefonnummer", "class":"form-control"}), label="")
	m2 = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"m2", "class":"form-control"}), label="")
	Kommuneplan = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Kommuneplan", "class":"form-control"}), label="")
	Lokalplan = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Lokalplan", "class":"form-control"}), label="")
	Formål = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Formål", "class":"form-control"}), label="")

	class Meta:
		model = Record
		exclude = ("user",)

class CommentForm(forms.ModelForm):
	class Meta: 
		model = Comment
		fields = ('name', 'body' )

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
		}

class ImportRecordDataForm(forms.Form):
    record_data = forms.FileField(required=True)



class CheckboxForm(forms.Form):
    class Meta:
        model = Record
        fields = ['Ja', 'Nej', 'Sendt til DLA']

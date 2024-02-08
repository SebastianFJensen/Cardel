from django import forms
from django.contrib.auth.models import User
from .models import Record, Comment, Folder, File
from mptt.forms import TreeNodeChoiceField

class AddRecordForms(forms.ModelForm):
    BFE_Nummer = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"BFE Nummer", "class":"form-control"}), label="")
    Adresse = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Adresse", "class":"form-control"}), label="")
    Kommune = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Kommune", "class":"form-control"}), label="")
    Region = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Region", "class":"form-control"}), label="")
    Kontaktperson = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Kontaktperson", "class":"form-control"}), label="")
    Mail = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Mail", "class":"form-control"}), label="")
    Telefonnummer = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Telefonnummer", "class":"form-control"}), label="")
    m2 = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"m2", "class":"form-control"}), label="")
    Kommuneplan = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Kommuneplan", "class":"form-control"}), label="")
    Lokalplan = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Lokalplan", "class":"form-control"}), label="")
    Formaal = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Formål", "class":"form-control"}), label="")
    Pris_Hektar = forms.DecimalField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Formål", "class":"form-control"}), label="")
    Moedestatus = forms.ChoiceField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Record
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        super(AddRecordForms, self).__init__(*args, **kwargs)

        status = self.data.get('Status')
        if status and status != 'Vælg' and status != 'Møde booket':
            self.fields['Moedestatus'].widget = forms.HiddenInput()
        elif status and status == 'Møde booket':
            self.fields['Moedestatus'].required = True
            self.fields['Moedestatus'].widget = forms.Select()
            self.fields['Moedestatus'].choices = Record.Moedestatus

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('Status')
        moedestatus = cleaned_data.get('Moedestatus')

        if status and status == 'Møde booket' and not moedestatus:
            self.add_error('Moedestatus', 'Vælg venligst en møde status')

    def save(self, commit=True):
        record = super().save(commit=False)
        record.save()
        return record

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        if self.user:
            comment.user = self.user
        if commit:
            comment.save()
        return comment

class ImportRecordDataForm(forms.Form):
    record_data = forms.FileField(required=True)



class CheckboxForm(forms.Form):
    class Meta:
        model = Record
        fields = ['Ja', 'Nej', 'Sendt til DLA']



class NewFolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['record', 'name']

    def __init__(self, *args, **kwargs):
        super(NewFolderForm, self).__init__(*args, **kwargs)
        self.fields['record'].queryset = Record.objects.all()

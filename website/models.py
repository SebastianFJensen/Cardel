from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from import_export import resources
from django.db.models.signals import post_save
from mptt.models import MPTTModel, TreeForeignKey
import uuid
import os
import unicodedata 


class Record(models.Model):
    Ansvarlig = {
        ('Benjamin', 'BENJAMIN'),
        ('Jakob', 'JAKOB'),
        ('Magnus', 'MAGNUS'),
        ('Stefan', 'Stefan'),
        ('Thomas', 'THOMAS'),
        ('Vælg', 'Vælg'),
    }
    Typen = {
        ('Negotiation','NEGOTIATION'),
        ('Sendt til DLA', 'SENDT TIL DLA'),
        ('Lead', 'LEAD'),
        ('Lukket aftale', 'LUKKET AFTALE'),
        ('Lost', 'LOST'),
        ('Møde booket', 'MØDE BOOKET'),
        ('Afventer underskrift', 'AFVENTER UNDERSKRIFT'),
        ('Vælg', 'Vælg')
    }
    Moedestatus = {
    ('Ombook', 'OMBOOK'),
    ('Møde afholdt', 'MØDE AFHOLDT'),
    ('Møde aflyst', 'MØDE AFLYST'),
    ('Vælg', 'Vælg')
    }
    created_at = models.DateTimeField(auto_now_add=True)
    BFE_Nummer = models.CharField(max_length=20)
    Adresse = models.CharField(max_length=20)
    Kommune = models.CharField(max_length=20)
    Region = models.CharField(max_length=20)
    Kontaktperson = models.CharField(max_length=20)
    Mail = models.CharField(max_length=20)
    Telefonnummer = models.CharField(max_length=20)
    m2 = models.CharField(max_length=20)
    Kommuneplan = models.CharField(max_length=20, blank=True)
    Lokalplan = models.CharField(max_length=20, blank=True)
    Formaal = models.CharField(max_length=50, blank=True)
    Status = models.CharField(max_length=20, choices=Typen, default='Vælg')
    Lead = models.CharField(max_length=10, choices=Ansvarlig, default='Vælg')
    Pris_Hektar = models.DecimalField(max_digits=20, decimal_places=2)
    id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return(f"{self.BFE_Nummer}")



class Comment(models.Model):
    post = models.ForeignKey(Record, related_name="comments", on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
    	return f"{self.post.BFE_Nummer}"


class RecordResource(resources.ModelResource):
    class Meta:
        model = Record
        import_id_fields = ["BFE_Nummer"]
        skip_unchanged = True
        use_bulk = True

def get_file_location(instance, filename):
    return f"{instance.folder.record.id}/{filename}/{unicodedata.normalize('NFKD', filename).encode('ascii', 'ignore').decode()}"

class Folder(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE, related_name='folders')
    name = models.CharField(max_length=60)
    folder_type = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.record.id} - {self.folder_type}"

@receiver(post_save, sender=Record)
def create_folder(sender, instance, created, **kwargs):
    if created:
        folder_types = ['Aftaler', 'Økonomi', 'Planer', 'Bilag']
        for folder_type in folder_types:
            Folder.objects.create(record=instance, name=folder_type, folder_type=folder_type)

class File(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, related_name='allfiles')
    files = models.FileField(upload_to=get_file_location)

    def __str__(self):
        return f"{self.files}"
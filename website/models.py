from django.db import models
from django.contrib.auth.models import User
from import_export import resources
import uuid


class Record(models.Model):
    Ansvarlig = {
        ('Benjamin', 'BENJAMIN'),
        ('Jakob', 'JAKOB'),
        ('Magnus', 'MAGNUS'),
        ('Stefan', 'Stefan'),
        ('Thomas', 'THOMAS'),
        ('Vælg', 'Vælg'),
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
    Kommuneplan = models.CharField(max_length=20)
    Lokalplan = models.CharField(max_length=20)
    Formål = models.CharField(max_length=20)
    Sendt_til_DLA = models.BooleanField(default=False)
    Lead = models.CharField(max_length=10, choices=Ansvarlig, default='Vælg')

    def __str__(self):
        return(f"{self.BFE_Nummer}")



class Comment(models.Model):
    post = models.ForeignKey(Record, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return '%s - %s' % (self.post.BFE_Nummer, self.name)


class RecordResource(resources.ModelResource):
    class Meta:
        model = Record
        import_id_fields = ["BFE_Nummer"]
        skip_unchanged = True
        use_bulk = True

class Folder(models.Model):
    foldername = models.CharField(max_length=50)
    description = models.CharField(max_length=200,blank=True,null=True)
    folderuser = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.foldername)

class File(models.Model):
    filename = models.CharField(max_length=100)
    file = models.FileField(upload_to='Files')
    folder = models.ForeignKey(Folder,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.filename)
from django.contrib import admin
from django.urls import path, include
from import_export.admin import ImportExportModelAdmin
from .models import Record, Comment, Folder, File

class RecordAdmin(ImportExportModelAdmin):
	pass

class AdminFolder(admin.ModelAdmin):
    list_display = ('foldername','folderuser')

class AdminFile(admin.ModelAdmin):
    list_display = ('filename','file')

admin.site.register(Record,RecordAdmin)
admin.site.register(Comment)
admin.site.register(Folder,AdminFolder)
admin.site.register(File,AdminFile)
path('', include('ccrm.urls'))

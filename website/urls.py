from django.urls import path
from . import views 
from .views import AddCommentView, import_from_excel
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('Record/<int:pk>', views.customer_record, name='Record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('importrecorddata', views.ImportRecordData.as_view(), name='importrecorddata'),
    path('Record/<int:pk>/comment/', views.AddCommentView.as_view(), name='add_comment1'),
    path('import/', import_from_excel, name='import_from_excel'),
    path('folder/<int:folderid>/',views.folder,name="folder"),
    path('delete/folder/<int:folderid>/',views.deleteFolder,name="delete-folder"),
    path('addFolder/',views.addFolder,name="addFolder"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
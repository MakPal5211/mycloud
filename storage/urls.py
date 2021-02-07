from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
    path('storage/', views.st_list, name='st_list'),
    path('storage/upload/', views.upload_file, name='upload_file'),
    path('storage/<int:pk>/', views.delete_file, name='delete_file'),

    # path('class/books/', views.BookListView.as_view(), name='class_book_list'),
    # path('class/books/upload/', views.UploadBookView.as_view(), name='class_upload_book'),

    path('admin/', admin.site.urls),
]
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import StForm
from .models import Storage


class Home(TemplateView):
    template_name = 'storage/home.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'storage/upload.html', context)


def st_list(request):
    files = Storage.objects.all()
    return render(request, 'storage/st_list.html', {
        'files': files
    })


def upload_file(request):
    if request.method == 'POST':
        form = StForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('st_list')
    else:
        form = StForm()
    return render(request, 'storage/upload_file.html', {
        'form': form
    })


def delete_file(request, pk):
    if request.method == 'POST':
        file = Storage.objects.get(pk=pk)
        file.delete()
    return redirect('st_list')


# class BookListView(ListView):
#     model = Book
#     template_name = 'storage/class_book_list.html'
#     context_object_name = 'books'
#
#
# class UploadBookView(CreateView):
#     model = Book
#     form_class = BookForm
#     success_url = reverse_lazy('class_book_list')
#     template_name = 'storage/upload_file.html'

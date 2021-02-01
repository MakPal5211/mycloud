from django.db import models
from django.conf import settings


class Book(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          related_name='file_saved',
    #                          on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

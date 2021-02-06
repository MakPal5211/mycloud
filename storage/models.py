from django.db import models
from django.conf import settings


class Book(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          related_name='file_saved',
    #                          on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    attached_file = models.FileField(upload_to='storage/files/')
    cover = models.ImageField(upload_to='storage/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.attached_file.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)

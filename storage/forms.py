from django import forms

from .models import Storage


class StForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = ('title', 'user', 'attached_file', 'cover')


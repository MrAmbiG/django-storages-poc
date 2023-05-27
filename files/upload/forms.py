from django import forms
from django.forms import ModelForm
from .models import FileModel

class FileForm(ModelForm):
    class Meta:
        model = FileModel
        fields = '__all__'

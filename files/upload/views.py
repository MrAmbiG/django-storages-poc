from django.shortcuts import render
from config import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import FileForm
from .models import FileModel

def home(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = FileModel(userfile=request.FILES["userfile"])
            instance.save()
            return HttpResponseRedirect("/")
    else:
        form = FileForm()
    return render(request, "home.html", {"form": form})

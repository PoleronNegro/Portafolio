from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def inicio(request):
    return render(request,'donia_clarita/inicio.html')
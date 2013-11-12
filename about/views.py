from django.http import HttpResponse
from about.models import About
from django.shortcuts import get_object_or_404, render, redirect

def index(request):
    about_list = About.objects()
    return render(request, 'about/about-index.html')

def agent(request):
    return render(request, 'about/about-staff.html')

def directors(request):
    return render(request, 'about/about-directors.html')

def one_director(request, name):
    return render(request, 'about/about-staff.html')

def vision(request):
    return redirect('grhuorg.views.vision', permanent=True)

def mission(request):
    return redirect('grhuorg.views.vision', permanent=True)

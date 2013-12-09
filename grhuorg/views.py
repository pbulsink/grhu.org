from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.template import RequestContext

def index(request):
    return render(request, 'grhuorg/index.html')

def home(request):
    return redirect('grhuorg.views.index', permanent=True)

def terms(request):
    return render(request, 'grhuorg/terms.html')

def privacy(request):
    return render(request, 'grhuorg/privacy.html')

def sitemap(request):
    return render(request, 'grhuorg/sitemap.html')

def vision(request):
    return render(request, 'grhuorg/vision.html')

def contact(request):
    return render(request, 'grhuorg/contact.html')

def helpout(request):
    return render(request, 'grhuorg/help-out.html')

def donate(request):
    return render(request, 'grhuorg/donate.html')

def mission(request):
    return redirect('grhuorg.views.vision', permanent=True)



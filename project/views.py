from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the projects index.")

def details(request, project_id):
    return HttpResponse("Hello, you're at the %s page" % project_id)

def shoes(request):
    return HttpResponse("Hello, you're at the shoes page")


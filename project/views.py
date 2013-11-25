from django.shortcuts import render, get_object_or_404
from project.models import Project

from django.http import HttpResponse

def index(request):
    lead = Project.objects.all().order_by('-pub_date')[0]
    latest_project_list = Project.objects.all().order_by('-pub_date')[1:10]
    context = {
        'items': latest_project_list,
        'lead': lead,
        'active_page': 'project',
        'urlpointertype': 'project',
        }
    return render(request, 'project/front.html', context)

def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {
        'article': project,
        'active_page': project
    }
    return render(request, 'project/article.html', context)

def list(request, list_pg=1):
    list_pg = int(list_pg)
    startno = 0 + (list_pg-1)*10
    endno = 9 + (list_pg-1)*10
    later_pages = True
    earlier_pages = True
    total_articles = Project.objects.count()
    if startno > total_articles:
        return 404
    if endno >= total_articles:
        endno = total_articles
        later_pages = False
    else:
        #For some reason the 0 and 1 index mixing isn't friendly. This is a temp fix
        endno+=1
    if startno == 0:
        earlier_pages = False
        
    project_list = Project.objects.all().order_by('-pub_date')[startno:endno]
    context = {
        'items': project_list,
        'active_page': 'project',
        'later_pages': later_pages,
        'earlier_pages': earlier_pages,
        'start_number': startno+1,
        'end_number': endno,
        'total_articles': total_articles,
        'list_pg': list_pg,
        'list_previous': list_pg-1,
        'list_next': list_pg+1
    }
    return render(request, 'project/list.html', context)

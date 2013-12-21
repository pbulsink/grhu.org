from django.shortcuts import render, get_object_or_404, render_to_response
from django.shortcuts import redirect, get_list_or_404, Http404
from django.template import RequestContext
from django.views.decorators.cache import never_cache
from project.models import Project

from django.http import HttpResponse

def index(request):
    projects_list = get_list_or_404(
        Project.objects.order_by('-start_date'),
        public=True
        )[:5]
    lead = projects_list[0]
    projects_list = projects_list[1:]
    context = {
        'items': projects_list,
        'lead': lead,
        }
    return render_to_response('project/front.html', context,
                              context_instance=RequestContext(request))

def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if not project.public:
        return Http404
    context = {
        'article': project,
    }
    return render_to_response('project/article.html', context,
                              context_instance=RequestContext(request))

def project_finder(request, url):
    if url == 'shoes':
        query = 'shoes'
    else:
        return Http404
    
    project = get_list_or_404(
        short_query = 'shoes',
        public=True
    )
    
    return redirect('project-detail', project_id = project.pk)

def list(request, list_pg=1):
    list_pg = int(list_pg)
    startno = 0 + (list_pg-1)*10
    endno = 9 + (list_pg-1)*10
    later_pages = True
    earlier_pages = True
    total_articles = Project.objects.count()
    if startno > total_articles:
        return Http404
    if endno >= total_articles:
        endno = total_articles
        later_pages = False
    else:
        #For some reason the 0 and 1 index mixing isn't friendly. This is a temp fix
        endno+=1
    if startno == 0:
        earlier_pages = False
        
    project_list = Project.objects.filter(public=True).order_by('-pub_date')[startno:endno]
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
    return render_to_response('project/list.html', context,
                              context_instance=RequestContext(request))

@never_cache
def latest(request):
    latest = get_list_or_404(
        Project.objects.order_by('-pub_date'),
        public = True
        )[:1]
    lead = latest[0]
    context = {
        'article': latest,
    }
    return render_to_response('project/article.html', context,
                              context_instance=RequestContext(request))

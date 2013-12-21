from django.shortcuts import render, get_object_or_404, Http404, get_list_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import never_cache
from blog.models import Blog

from django.http import HttpResponse

def index(request):
    latest_blog_list = get_list_or_404(
        Blog.objects.order_by('-pub_date'),
        public = True
        )[:11]
    lead = latest_blog_list[0]
    latest_blog_list = latest_blog_list[1:]
    context = {
        'items': latest_blog_list,
        'lead': lead,
        }
    return render_to_response('blog/front.html', context,
                              context_instance=RequestContext(request))

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if not blog.public:
        return Http404
    context = {
        'article': blog,
    }
    return render_to_response('blog/article.html', context,
                              context_instance=RequestContext(request))

def list(request, list_pg=1):
    list_pg = int(list_pg)
    startno = 0 + (list_pg-1)*10
    endno = 9 + (list_pg-1)*10
    later_pages = True
    earlier_pages = True
    all_articles = Blog.objecst.filter(public=True).order_by('-pub_date')
    total_articles = len(all_articles)
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
        
    blog_list = all_articles[startno:endno]
    context = {
        'items': blog_list,
        'active_page': 'blog',
        'later_pages': later_pages,
        'earlier_pages': earlier_pages,
        'start_number': startno+1,
        'end_number': endno,
        'total_articles': total_articles,
        'list_pg': list_pg,
        'list_previous': list_pg-1,
        'list_next': list_pg+1
    }
    return render_to_response('blog/list.html', context,
                              context_instance=RequestContext(request))

@never_cache
def latest(request):
    latest = get_list_or_404(
        Blog.objects.order_by('-pub_date'),
        public = True
        )[:1]
    lead = latest[0]
    context = {
        'article': latest,
    }
    return render_to_response('blog/article.html', context,
                              context_instance=RequestContext(request))

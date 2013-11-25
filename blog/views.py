from django.shortcuts import render, get_object_or_404
from blog.models import Blog

from django.http import HttpResponse

def index(request):
    lead = Blog.objects.all().order_by('-pub_date')[0]
    latest_blog_list = Blog.objects.all().order_by('-pub_date')[1:10]
    context = {
        'items': latest_blog_list,
        'lead': lead,
        'active_page': 'blog',
        'urlpointertype': 'blog',
        }
    return render(request, 'blog/front.html', context)

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'article': blog,
        'active_page': blog
    }
    return render(request, 'blog/article.html', context)

def list(request, list_pg=1):
    list_pg = int(list_pg)
    startno = 0 + (list_pg-1)*10
    endno = 9 + (list_pg-1)*10
    later_pages = True
    earlier_pages = True
    total_articles = Blog.objects.count()
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
        
    blog_list = Blog.objects.all().order_by('-pub_date')[startno:endno]
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
    return render(request, 'blog/list.html', context)

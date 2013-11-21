from django.shortcuts import render, get_object_or_404
from news.models import News

from django.http import HttpResponse

def index(request):
    lead = News.objects.all().order_by('-pub_date')[0]
    latest_news_list = News.objects.all().order_by('-pub_date')[1:10]
    context = {
        'items': latest_news_list,
        'lead': lead,
        'active_page': 'news',
        'urlpointertype': 'news',
        }
    return render(request, 'news/front.html', context)

def detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    context = {
        'article': news,
        'active_page': news
    }
    return render(request, 'news/article.html', context)

def list(request, list_pg=1):
    list_pg = int(list_pg)
    startno = 0 + (list_pg-1)*10
    endno = 9 + (list_pg-1)*10
    later_pages = True
    earlier_pages = True
    total_articles = News.objects.count()
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
        
    news_list = News.objects.all().order_by('-pub_date')[startno:endno]
    context = {
        'items': news_list,
        'active_page': 'news',
        'later_pages': later_pages,
        'earlier_pages': earlier_pages,
        'start_number': startno+1,
        'end_number': endno,
        'total_articles': total_articles,
        'list_pg': list_pg,
        'list_previous': list_pg-1,
        'list_next': list_pg+1
    }
    return render(request, 'news/list.html', context)

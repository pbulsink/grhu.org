from django.shortcuts import render
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
    return render(request, '_front.html', context)

def detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    context = {
        'article': news,
        'active_page': 'news',
    }
    return render(request, '_article.html', context)

def list(request, list_pg=1):
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
    if startno == 0:
        earlier_pages = False
        
    news_list = News.objects.all().order_by('-pub_date')[startno:endno]
    context = {
        'items': news_list,
        'active_page': 'news',
        'later_pages': later_pages,
        'earlier_pages': earlier_pages,
        'start_number': startno+1,
        'end_number': endno+1,
        'total_articles': total_articles,
        'list_pg': list_pg,
        'urlpointertype': 'news.lister'
    }
    return render(request, '_list.html', context)

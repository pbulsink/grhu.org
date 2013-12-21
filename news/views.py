from django.shortcuts import render, get_object_or_404, Http404
from django.shortcuts import render_to_response, get_list_or_404
from django.template import RequestContext
from django.views.decorators.cache import never_cache
from news.models import News


def index(request):
    latest_news_list = get_list_or_404(
        News.objects.order_by('-pub_date'),
        public=True
        )[:11]
    lead = latest_news_list[0]
    latest_news_list = latest_news_list[1:]
    context = {
        'items': latest_news_list,
        'lead': lead,
        }
    return render_to_response('news/front.html', context,
                              context_instance=RequestContext(request))


def detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    if not news.public:
        return Http404
    context = {
        'article': news,
    }
    return render_to_response('news/article.html', context,
                              context_instance=RequestContext(request))


def list(request, list_pg=1):
    list_pg = int(list_pg)
    startno = 0 + (list_pg-1)*10
    endno = 9 + (list_pg-1)*10
    later_pages = True
    earlier_pages = True
    all_articles = News.objects.filter(
        public=True
        ).order_by('-pub_date')
    total_articles = len(all_articles)
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
        
    news_list = all_articles[startno:endno]
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
    return render_to_response('news/list.html', context,
                              context_instance=RequestContext(request))

@never_cache
def latest(request):
    latest = get_list_or_404(
        News.objects.order_by('-pub_date'),
        public = True
        )[:1]
    lead = latest[0]
    context = {
        'article': latest,
    }
    return render_to_response('news/article.html', context,
                              context_instance=RequestContext(request))

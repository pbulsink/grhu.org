from django.shortcuts import render, get_object_or_404
from press.models import Press

from django.http import HttpResponse

def index(request):
    lead = Press.objects.get(public=True).order_by('-pub_date')[0]
    latest_press_list = Press.objects.get(public=True).order_by('-pub_date')[1:10]
    context = {
        'items': latest_press_list,
        'lead': lead,
        }
    return render(request, 'press/front.html', context)

def detail(request, press_id):
    press = get_object_or_404(Press, pk=press_id)
    if not press.public:
        return Http404
    context = {
        'article': press,
    }
    return render(request, 'press/article.html', context)

def list(request, list_pg=1):
    list_pg = int(list_pg)
    startno = 0 + (list_pg-1)*10
    endno = 9 + (list_pg-1)*10
    later_pages = True
    earlier_pages = True
    all_articles = Press.objects.get(public=True).order_by('-pub_date')
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
        
    press_list = all_articles[startno:endno]
    context = {
        'items': press_list,
        'active_page': 'press',
        'later_pages': later_pages,
        'earlier_pages': earlier_pages,
        'start_number': startno+1,
        'end_number': endno,
        'total_articles': total_articles,
        'list_pg': list_pg,
        'list_previous': list_pg-1,
        'list_next': list_pg+1
    }
    return render(request, 'press/list.html', context)

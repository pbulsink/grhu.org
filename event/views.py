from event.models import Event
from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render_to_response, Http404, get_list_or_404
from django.template import RequestContext
from django.views.decorators.cache import never_cache
from datetime import datetime  

def index(request):
    event_list = get_list_or_404(
        Event.objects.order_by('-start'),
        public = True
        )[:3]
    event = event_list[0]
    event_list = event_list[1:]
    context = {
        'event': event,
        'items': event_list,
    }
    return render_to_response('event/front.html', context,
                              context_instance=RequestContext(request))

def upcoming(request):
    event_list = get_list_or_404(
        Event.objects.order_by('-date'),
        date > datetime.today(),
        public = True
        )
    if event_list:
        if len(event_list) > 1:
            event = event_list[0]
            event_list = event_list[1:]
            context = {
                'event': event,
                'items': event_list
            }
        else:
            context = {
                'event' : event_list
            }
    context['titlemod'] = 'Upcoming '    
    return render_to_response('event/front.html', context,
                              context_instance=RequestContext(request))

def recent(request):
    event_list = get_list_or_404(
        Event.objects.order_by('-date'),
        date < datetime.today(),
        date.year > datetime.today().year-2,
        public = True
        )
    if event_list:
        if len(event_list) > 1:
            event = event_list[0]
            event_list = event_list[1:]
            context = {
                'event': event,
                'items': event_list
            }
        else:
            context = {
                'event' : event_list
            }
    context['titlemod'] = 'Recent '
    return render_to_response('event/front.html', context,
                              context_instance=RequestContext(request))

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if not event.public:
        return Http404
    context = {
        'article': event,
    }
    return render_to_response('event/article.html', context,
                              context_instance=RequestContext(request))

def list(request, list_pg=1):
    list_pg = int(list_pg)
    startno = 0 + (list_pg-1)*10
    endno = 9 + (list_pg-1)*10
    later_pages = True
    earlier_pages = True
    all_articles = Event.objects.filter(
        public=True
        ).order_by('-pub_date')
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
        
    event_list = all_articles[startno:endno]
    context = {
        'items': event_list,
        'later_pages': later_pages,
        'earlier_pages': earlier_pages,
        'start_number': startno+1,
        'end_number': endno,
        'total_articles': total_articles,
        'list_pg': list_pg,
        'list_previous': list_pg-1,
        'list_next': list_pg+1
    }
    return render_to_response('event/list.html', context,
                              context_instance=RequestContext(request))

@never_cache
def latest(request):
    latest = get_list_or_404(
        Event.objects.order_by('-pub_date'),
        public = True
        )[:1]
    lead = latest[0]
    context = {
        'article': latest,
    }
    return render_to_response('event/article.html', context,
                              context_instance=RequestContext(request))

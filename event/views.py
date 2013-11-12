from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from event.models import Event

def index(request):
    first_event = Event.objects.order_by('-event_date')[0]
    event_list = Event.objects.order_by('-event_date')[1:3]
    preamble = ("GRHU periodically puts on events throughout the year. If you're "
                "interested in helping out with any events, whether planning, "
                "volunteering on the day of an event, or running your own event "
                "entirely, <a href=\"{% url 'grhuorg.views.helpout' %}\">read "
                "more</a> about how to help out and where we have volunteer opportunities.")
    context = {'first_item': first_event,
               'list': event_list,
               'preamble': preamble,
               'pagetitle': "Events",
               'active_page': "events",
               'active_nav' : "none",
               'active_detail_url' : 'detail',
               }
    return render(request, '_list.html', context)

def upcoming(request):
    event_list = Event.objects
    return HttpResponse("Hello, you're at the upcoming events.")

def past(request):
    return HttpResponse("Hello, you're at the past events.")

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return HttpResponse("You're looking at event %s." % event_id)



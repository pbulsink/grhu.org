from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.decorators.cache import never_cache

def index(request):
    return HttpResponse("You're at the photoalbums index")

@never_cache
def latest(request):
    latest = get_list_or_404(
        Album.objects.order_by('-pub_date'),
        public = True
        )[:1]
    lead = latest[0]
    context = {
        'article': latest,
    }
    return render_to_response('album/article.html', context,
                              context_instance=RequestContext(request))

from about.models import About
from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render_to_response, get_list_or_404
from django.template import RequestContext

def index(request):
    about_list = get_list_or_404(
        About,
        public=True
        )

    director_list = []
    board_list = []
    general = []
    agent_list = []
    
    for about in about_list:
        if about.about_type == "General":
            general.append(about)
        elif about.about_type == "Director":
            director_list.append(about)
        elif about.about_type == "Agent":
            agent_list.append(about)
        elif about.about_type == "Board":
            board_list.append(about)

    print general
    
    context = {
        "directors":director_list,
        "boards":board_list,
        "general":general[0],
        "agents":agent_list,
    }
    return render_to_response('about/front.html', context,
                              context_instance=RequestContext(request))

    
def list(request, staff_type=None):
    if staff_type:
        staff_list = get_list_or_404(
            About,
            about_type=staff_type,
            public=True)
        staff_type += 's'
    else:
        staff_type = 'Staff'
        staff_list = get_list_or_404(About)
        for staff in staff_list[:]:
            if staff.about_type == "General" or staff.about_type == "Boilerplate":
                staff_list.remove(staff)
    #if len(staff_list) == 1:
    #    return redirect('about-staff', staff_list[0].id)
    context={
        'active_page': 'about',
        'ptitle': staff_type,
        'staff': staff_list
    }
    return render_to_response('about/list.html', context,
                              context_instance=RequestContext(request))


def staff(request, staff_id):
    staff = get_object_or_404(About, pk=staff_id)
    if not staff.public:
        return Http404
    context = {
        'article': staff,
    }
    return render_to_response('about/staff.html', context,
                              context_instance=RequestContext(request))

from about.models import About
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.text import slugify


def index(request):
    about_list = About.objects.get(public=True)
    director_list = list()
    board_list = list()
    general = list()
    agent_list = list()
    
    for about in about_list:
        if about.about_type == "General":
            general.append(about)
        elif about.about_type == "Director":
            director_list.append(about)
        elif about.about_type == "Agent":
            agent_list.append(agent)
        elif about.about_type == "Board":
            board_list.append(about)
    
    context = {
        "directors":director_list,
        "boards":board_list,
        "general":general,
        "agents":agent_list,
    }
    return render(request, 'about/front.html', context)


def agents(request):
    agent_list = About.objects.get(about_type="Agent", public=True)
    if len(agent_list) == 1:
        return redirect('about-staff', agent_list[0].id)
    context={
        'active_page': 'about',
        'title': 'Agents',
        'staff': agent_list
    }
    return render(request, 'about/list.html', context)
    

def directors(request):
    director_list = About.objects.get(about_type="Director", public=True)
    if len(agent_list) == 1:
        return redirect('about-staff', director_list[0].id)
    context={
        'active_page': 'about',
        'title': 'Directors',
        'staff': director_list
    }
    return render(request, 'about/list.html', context)


def one_director(request, req_name):
    director_list = About.objects.get(about_type="Director", public=True)
    names=list()
    for director in director_list:
        names.append((str(director.name).lower(), director.id))
        names.append((str(director.first_name()).lower(), director.id))
        names.append((slugify(director.name).lower(), director.id))
        names.append((slugify(director.first_name()), director.id))
    dir_id=None
    req_name=str(req_name).lower()
    for name in names:
        if name[0] == req_name:
            dir_id = name[1]
            break
    if dir_id:
        return redirect('about-staff', staff_id=dir_id, permanent=True)
    else:
        return redirect('about-list')


def staff(request, staff_id):
    staff = get_object_or_404(About, pk=staff_id)
    if not staff.public:
        return Http404
    context = {
        'article': staff,
    }
    return render(request, 'about/staff.html', context)


def vision(request):
    return redirect('grhuorg.views.vision', permanent=True)


def mission(request):
    return redirect('grhuorg.views.vision', permanent=True)

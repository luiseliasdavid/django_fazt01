from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Project,Task

# Create your views here.
def index(request):
    title = 'welcome to django curse'
    return render(request,"index.html", {
        'title': title
    })


def hello(request,username):
    """ruta saludar con param"""
    return HttpResponse("<h2>  hello %s </h2>" % username )

def about(request):
    """ruta about"""
    username= 'Luis David'
    return render(request,"about.html",{
        'username':username
    })

def projects(request):
    """ consulta a la base de datos """
    projects = list(Project.objects.values())
    return render(request,"projects.html",{
        'projects':projects
    })

def tasks(request):
    #task = get_object_or_404(Task, title=title)
    return render(request,"tasks.html")

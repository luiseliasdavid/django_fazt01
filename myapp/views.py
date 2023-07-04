from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Project,Task
from .forms import CreateNewTask , CreateNewProject

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
    tasks = Task.objects.all()
    return render(request,"tasks.html",{
        'tasks':tasks
    })

def create_task(request):
    if request.method == 'GET':
          return render(request,"create_task.html", {
        'form': CreateNewTask()
         })
    else:
         Task.objects.create(title=request.POST['title'],
                        description=request.POST['description'],project_id=1)
         return redirect('tasks')  

def create_project(request):
    if request.method == 'GET':
        return render(request, 'create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect('project') 
    
def project_detail(request,id):
    project = get_object_or_404(Project,id=id)
    tasks = Task.objects.filter(project_id=id)
    print(project)
    return render(request, 'project_detail.html',{
        'project': project,
        'tasks' : tasks
    })

   
    

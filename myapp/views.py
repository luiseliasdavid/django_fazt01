from django.http import HttpResponse, JsonResponse
from .models import Project,Task

# Create your views here.
def index(request):
    return HttpResponse("<h2> index page </h2>")


def hello(request,username):
    """ruta saludar con param"""
    return HttpResponse("<h2>  hello %s </h2>" % username )

def about(request):
    """ruta about"""
    return HttpResponse("<h2> About </h2>")

def projects(request):
    """ consulta a la base de datos """
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, id):
    task = Task.objects.get(id=id)
    print('hola que tal ',task)
    return HttpResponse('task: %s' % task.title)

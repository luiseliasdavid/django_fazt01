from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("<h2>  hello world </h2>")

def about(request):
    return HttpResponse("<h2> About </h2>")

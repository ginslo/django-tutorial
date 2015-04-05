from django.http import HttpResponse
import datetime

# def index(request):
#     return HttpResponse("Hello world")
    
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    
class AboutView(HttpResponse):
    template_name = 'about.html'
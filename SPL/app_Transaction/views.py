from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('app_Transaction/index.html')
    #return HttpResponse(template.render(request))
    return HttpResponse("Hello, world. You're at the app_Transaction index.")

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the app_Another_Action index.")

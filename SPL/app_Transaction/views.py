from django.http import HttpResponse
from django.template import loader

from .models import User


def index(request):
    return HttpResponse("Hello, world. You're at the index view.")
    '''
    # Below is an attempt to implement test code from the example
    template = loader.get_template('app_Transaction/index.html')
    return HttpResponse(template.render(context, request))
    '''
# This is where we define our other views


def registration(request):
    return HttpResponse("Hello, world. You're at the registration view.")


def checkPolyCardData(request, iso_Number):
    # return
    pass


'''
def checkIn_Or_CheckOut(request):
    return HttpResponse("Hello, world. You're at the checkIn_Or_CheckOut view.")

def checkOut(request):
    return HttpResponse("Hello, world. You're at the checkOut view.")

def regular_CheckOut(request):
    return HttpResponse("Hello, world. You're at the regular_CheckOut view.")

def express_CheckOut(request):
    return HttpResponse("Hello, world. You're at the express_CheckOut view.")

def checkIn(request):
    return HttpResponse("Hello, world. You're at the checkIn view.")

def another_Action(request):
    return HttpResponse("Hello, world. You're at the another_Action view.")

def transaction_Summary(request):
    return HttpResponse("Hello, world. You're at the transaction_Summary view.")
'''

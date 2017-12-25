from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import User


def index(request):
    #return HttpResponse("Hello, world. You're at the index view.")
    return render(request, 'app_Transaction/index.html')

def registration(request):
    #return HttpResponse("Hello, world. You're at the registration view.")
    return render(request, 'app_Transaction/registration.html')

def checkPolyCardData(request):
    #numbers = [1,2,3,4,5]
    #name = 'Bill Gates'
    #args = {'myName' : name, 'numbers' : numbers}
    #                       location of template
    #return render(request, 'app_Transaction/checkPolyCard.html', args)
    return render(request, 'app_Transaction/checkPolyCard.html')

# This is where we define our other views

def checkIn_Or_CheckOut(request):
    #return HttpResponse("Hello, world. You're at the checkIn_Or_CheckOut view.")
    return render(request, 'app_Transaction/CheckInOrCheckOut.html')

def checkOut(request):
    #return HttpResponse("Hello, world. You're at the checkOut view.")
    return render(request, 'app_Transaction/checkOut.html')
'''
def regular_CheckOut(request):
    return HttpResponse("Hello, world. You're at the regular_CheckOut view.")

def express_CheckOut(request):
    return HttpResponse("Hello, world. You're at the express_CheckOut view.")
'''
def checkIn(request):
    #return HttpResponse("Hello, world. You're at the checkIn view.")
    return render(request, 'app_Transaction/checkIn.html')
'''
def another_Action(request):
    return HttpResponse("Hello, world. You're at the another_Action view.")
'''
def transaction_Summary(request):
    #return HttpResponse("Hello, world. You're at the transaction_Summary view.")
    return render(request, 'app_Transaction/transactionSummary.html')

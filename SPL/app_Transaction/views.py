from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

from .models import User
from app_Transaction.forms import RegistrationForm

# Define function-based views

def checkIn(request):
    return render(request, 'app_Transaction/checkIn.html')

def checkIn_Or_CheckOut(request):
    return render(request, 'app_Transaction/CheckInOrCheckOut.html')

def checkOut(request):
    return render(request, 'app_Transaction/checkOut.html')

def checkPolyCardData(request):
    #numbers = [1,2,3,4,5]
    #name = 'Bill Gates'
    #args = {'myName' : name, 'numbers' : numbers}
    #                       location of template
    #return render(request, 'app_Transaction/checkPolyCard.html', args)
    return render(request, 'app_Transaction/checkPolyCard.html')

def index(request):
    return render(request, 'app_Transaction/index.html')

def registration(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/app_Transaction')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'app_Transaction/registration.html', args)
    #return render(request, 'app_Transaction/registration.html')

def transaction_Summary(request):
    return render(request, 'app_Transaction/transactionSummary.html')

# Views yet to be implemented
'''
def regular_CheckOut(request):
    return HttpResponse("Hello, world. You're at the regular_CheckOut view.")

def express_CheckOut(request):
    return HttpResponse("Hello, world. You're at the express_CheckOut view.")

def another_Action(request):
    return HttpResponse("Hello, world. You're at the another_Action view.")
'''

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User
from app_Transaction.forms import RegistrationForm, CheckPolyCardForm

# Define function-based views

def checkIn(request):
    return render(request, 'app_Transaction/checkIn.html')

def checkIn_Or_CheckOut(request):
    return render(request, 'app_Transaction/CheckInOrCheckOut.html')

def checkOut(request):
    return render(request, 'app_Transaction/checkOut.html')

def checkPolyCardData(request):
    x = CheckPolyCardForm.save
    print (x)
    if request.method =='POST':
        checkPolyCardForm = CheckPolyCardForm(request.POST)
        if checkPolyCardForm.is_valid():
            checkPolyCardForm.save()
            #print (reverse('index'))
            #return reverse('index').lstrip('/')
            return redirect('/app_Transaction')
    else:
        checkPolyCardForm = CheckPolyCardForm()
        args = {'checkPolyCardForm': checkPolyCardForm}
        return render(request, 'app_Transaction/checkPolyCard.html', args)
    #numbers = [1,2,3,4,5]
    #name = 'Bill Gates'
    #args = {'myName' : name, 'numbers' : numbers}
    #                       location of template
    #return render(request, 'app_Transaction/checkPolyCard.html', args)
    return render(request, 'app_Transaction/checkPolyCard.html')

def index(request):
    return render(request, 'app_Transaction/index.html')

def registered_Users(request):
    all_Users = list(User.objects.all())
    i = 0
    registered_Users_List = []
    while i < len(all_Users):
        first_Name = User.objects.values('first_Name')[i]['first_Name']
        last_Name = User.objects.values('last_Name')[i]['last_Name']
        full_Name = first_Name + ' ' + last_Name
        registered_Users_List.append(full_Name)
        i += 1
    args = {'registered_Users_List': registered_Users_List}
    return render(request, 'app_Transaction/registeredUsers.html', args)

def registration(request):
    if request.method =='POST':
        registrationForm = RegistrationForm(request.POST)
        if registrationForm.is_valid():
            registrationForm.save()
            return redirect('/app_Transaction')
    else:
        registrationForm = RegistrationForm()
        args = {'registrationForm': registrationForm}
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

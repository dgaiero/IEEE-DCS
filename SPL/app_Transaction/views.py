from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Part
from app_Transaction.forms import RegistrationForm, CheckPolyCardForm
from app_Transaction.user_registration_scripts.polyCardData import getData

# Define function-based views

def checkIn(request):
    return render(request, 'app_Transaction/checkIn.html')

def checkIn_Or_CheckOut(request):
    return render(request, 'app_Transaction/CheckInOrCheckOut.html')

def checkOut(request):
    return render(request, 'app_Transaction/checkOut.html')

def checkPolyCardData(request):
    if request.method =='POST':
        checkPolyCardForm = CheckPolyCardForm(request.POST)
        if checkPolyCardForm.is_valid():
            raw_PolyCard_Data = checkPolyCardForm.cleaned_data['polyCard_Data']
            polyCardData = getData(raw_PolyCard_Data)
            print (polyCardData)

            registeredStatus = None
            validInput = None

            if polyCardData[1] == True:
                all_Users = list(User.objects.all())

                model_Attribute = 'polyCard_Data'

                i = 0
                while i < len(all_Users):
                    userInput = User.objects.values(model_Attribute)[i][model_Attribute]
                    if userInput == raw_PolyCard_Data:
                        print ('\nYou are already registered!\n')
                        registeredStatus = True
                        break
                    i += 1

                if registeredStatus == True:
                    print ('\nYou will be redirected to the checkInOrCheckOut page!\n')
                    validInput = True
                    #return render(request, 'app_Transaction/checkInOrCheckOut.html')
                    #return redirect('/app_Transaction/checkInOrCheckOut.html')
                    #return reverse('checkIn_Or_CheckOut')
                    return HttpResponseRedirect('/app_Transaction/checkInOrCheckOut')
                else:
                    print ('\nYou will be redirected to the register page!\n')
                    validInput = True
                    #return render(request, 'app_Transaction/registration.html')
                    #return redirect('/app_Transaction/registration/')
                    #return reverse('registration')
                    return HttpResponseRedirect('/app_Transaction/registration')
            else:
                print ('\nInvalid PolyCard! Please swipe a valid PolyCard!\n')
                validInput = False
                #return redirect('/app_Transaction/checkPolyCard')
                #return render(request, 'app_Transaction/checkPolyCard.html')
                #return reverse('checkPolyCardData')
                return HttpResponseRedirect('/app_Transaction/checkPolyCard')


            #checkPolyCardForm.save()
            #print (reverse('index'))
            #return reverse('index').lstrip('/')
            #return redirect('/app_Transaction')
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

def parts(request):
    all_Parts = list(Part.objects.all())
    i = 0
    registered_Parts_List = []
    total_Parts = len(all_Parts)
    while i < total_Parts:
        part = Part.objects.values('part')[i]['part']
        registered_Parts_List.append(part)
        i +=1
    registered_Parts_List = sorted(registered_Parts_List)
    args = {'registered_Parts_List': registered_Parts_List, 'total_Parts': total_Parts}
    return render(request, 'app_Transaction/parts.html', args)

def registered_Users(request):
    all_Users = list(User.objects.all())
    i = 0
    registered_Users_List = []
    total_Users = len(all_Users)
    while i < total_Users:
        first_Name = User.objects.values('first_Name')[i]['first_Name']
        last_Name = User.objects.values('last_Name')[i]['last_Name']
        full_Name = first_Name + ' ' + last_Name
        registered_Users_List.append(full_Name)
        i += 1
    args = {'registered_Users_List': registered_Users_List, 'total_Users': total_Users}
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

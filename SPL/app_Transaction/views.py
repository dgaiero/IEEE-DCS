from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Part
from app_Transaction.forms import RegistrationForm, CheckPolyCardForm, CheckOutForm
from app_Transaction.user_registration_scripts.polyCardData import getData

# try to include error messages here
def getJSONofCurrentUser(sessionData):
    currentUserData = User.objects.get(polyCard_Data=sessionData).__dict__
    return currentUserData
# Define function-based views

def another_Action(request):
    return render(request, 'app_Transaction/anotherAction.html')

def checkIn(request):
    return render(request, 'app_Transaction/checkIn.html')

def Logout(request):
    try:
        del request.session['polyCardData']
    except:
        print("Fail")
        pass
    return HttpResponse("<strong>You are logged out.</strong>")

def checkIn_Or_CheckOut(request):
    if request.session.has_key('polyCardData'):
        userData = getJSONofCurrentUser(request.session['polyCardData'])
        args = {'userFirstName':userData['first_Name']}
        return render(request, 'app_Transaction/CheckInOrCheckOut.html', args)
    else:
        return redirect('/app_Transaction/')

def checkOut(request):
    if request.session.has_key('polyCardData'):
        if request.method =='POST':
            checkOutForm = CheckOutForm(request.POST)
            if checkOutForm.is_valid():
                checkOutForm.save()
                return redirect('/app_Transaction/')
        else:
            checkOutForm = CheckOutForm()
            args = {'checkOutForm': checkOutForm}
            return render(request, 'app_Transaction/checkOut.html', args)
    else:
        return redirect('/app_Transaction/')
    '''
    all_Parts = list(Part.objects.all())
    i = 0
    registered_Parts_List = []
    quantity_List = []
    total_Parts = len(all_Parts)
    while i < total_Parts:
        part = Part.objects.values('part')[i]['part']
        quantity = Part.objects.values('quantity')[i]['quantity']
        registered_Parts_List.append(part)
        quantity_List.append(quantity)
        i += 1
    registered_Parts_List = sorted(registered_Parts_List)
    args = {'registered_Parts_List': registered_Parts_List,
            'total_Parts': total_Parts,
            'quantity_List': quantity_List,}
    return render(request, 'app_Transaction/checkOut.html', args)
    '''

def checkPolyCardData(request):
    if request.session.has_key('polyCardData'):
        return redirect('/app_Transaction/checkInOrCheckOut')
    else:
        if request.method =='POST':
            checkPolyCardForm = CheckPolyCardForm(request.POST)
            if checkPolyCardForm.is_valid():
                raw_PolyCard_Data = checkPolyCardForm.cleaned_data['polyCard_Data']
                polyCardData = getData(raw_PolyCard_Data)


                registeredStatus = None

                if polyCardData[1] == True:
                    all_Users = list(User.objects.all())

                    model_Attribute = 'polyCard_Data'

                    i = 0
                    while i < len(all_Users):
                        userInput = User.objects.values(model_Attribute)[i][model_Attribute]

                        if userInput == raw_PolyCard_Data:
                            registeredStatus = True
                            break
                        i += 1
                    if registeredStatus == True:
                        validInput = True
                        #request.session['polyCardData'] = User.objects.get(polyCard_Data=raw_PolyCard_Data).__dict__['polyCard_Data'])
                        request.session['polyCardData']=str(raw_PolyCard_Data)
                        return HttpResponseRedirect('/app_Transaction/checkInOrCheckOut')
                    else:
                        validInput = True
                        return HttpResponseRedirect('/app_Transaction/registration')
                else:
                    return HttpResponseRedirect('/app_Transaction/')

        else:
            checkPolyCardForm = CheckPolyCardForm()
            args = {'checkPolyCardForm': checkPolyCardForm}
            return render(request, 'app_Transaction/checkPolyCard.html', args)

        return render(request, 'app_Transaction/checkPolyCard.html')

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
            return redirect('/app_Transaction/')
    else:
        registrationForm = RegistrationForm()
        args = {'registrationForm': registrationForm}
        return render(request, 'app_Transaction/registration.html', args)

def transaction_Summary(request):
    if request.session.has_key('polyCardData'):
        userData = getJSONofCurrentUser(request.session['polyCardData'])
        return render(request, 'app_Transaction/transactionSummary.html')
    else:
        return redirect('/app_Transaction/')

# Views yet to be implemented
'''
def regular_CheckOut(request):
    return HttpResponse("Hello, world. You're at the regular_CheckOut view.")

def express_CheckOut(request):
    return HttpResponse("Hello, world. You're at the express_CheckOut view.")
'''

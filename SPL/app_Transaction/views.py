from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms
from pprint import pprint
import json
from .models import User, Part, userPart, eventLog
from django.core.exceptions import ObjectDoesNotExist
from app_Transaction.forms import RegistrationForm, studentLoginForm, CheckOutForm
from app_Transaction.user_registration_scripts.polyCardData import getData

# import os
# os.environ['DJANGO_SETTINGS_MODULE']='SPL.settings'


# try to include error messages here
def getJSONofCurrentUser(sessionData):
    currentUserData = User.objects.get(polyCard_Data=sessionData).__dict__
    return currentUserData
# Define function-based views


def logEventData(checkedOutTo, checkedOutBy, logType, content):
    newLogEvent = eventLog(checkedOutTo=checkedOutTo,
                           checkedOutBy=checkedOutBy, logType=logType, content=content)
    newLogEvent.save()


def another_Action(request):
    return render(request, 'app_Transaction/anotherAction.html')


def checkIn(request):
    userData = getJSONofCurrentUser(request.session['polyCardData'])

    all_Parts = list(userPart.objects.filter(userAssigned=User.objects.get(
        polyCard_Data=request.session['polyCardData'])))
    print(all_Parts)

    checkedOutPartsList = []

    for i in range(len(all_Parts)):
        partName = all_Parts[i].part
        partQty = all_Parts[i].quantity_Checked_Out
        partID = all_Parts[i].id_Number
        # partData = {"PartName": part, "PartQty": partQty}
        registered_Parts_inner = [partName, partQty, partID]
        checkedOutPartsList.append(registered_Parts_inner)


    args = {'registered_Parts_List': checkedOutPartsList,
            'userFirstName': userData['first_Name']}
    return render(request, 'app_Transaction/checkIn.html', args)


def studentLogout(request):
    try:
        del request.session['polyCardData']
    except:
        print("Fail")
        pass
    args = {'logoutFlag': "True"}
    return redirect('/app_Transaction/studentLogin/?logoutFlag=True', args)
    # return HttpResponse("<strong>You are logged out.</strong>")


def checkIn_Or_CheckOut(request):
    if request.session.has_key('polyCardData'):
        userData = getJSONofCurrentUser(request.session['polyCardData'])

        args = {'userFirstName': userData['first_Name']}
        return render(request, 'app_Transaction/CheckInOrCheckOut.html', args)
    else:
        return redirect('/app_Transaction/')


def checkOut(request):
    if request.session.has_key('polyCardData'):
        if request.method == 'POST':
            partData = json.loads(request.POST['partData'])
            userData = User.objects.get(
                polyCard_Data=request.session['polyCardData'])
            for key, value in partData.items():

                partName = value['partName']
                partQty = value['partQty']
                partID = value['partID']
                if partID == "":
                    partID = "N/A"
                print(partName)
                print(partQty)
                print(partID)
                part = Part.objects.get(part=partName)
                part.quantity_Checked_Out += int(partQty)
                part.save()
                # userData.parts.add(part)

                try:
                    partsCheckedOut = userPart.objects.get(
                        userAssigned=userData, part=partName)
                    partsCheckedOut.quantity_Checked_Out += int(partQty)
                    partsCheckedOut.save()
                except ObjectDoesNotExist:
                    newUserPart = userPart(
                        userAssigned=userData, part=partName, quantity_Checked_Out=partQty, id_Number=partID)
                    newUserPart.save()

                logginAction = "CHECKOUT: PART - {}, QTY - {}, ID - {}".format(
                    partName, partQty, partID)

            print("Success")
            return redirect('/app_Transaction/')
            # checkOutForm = CheckOutForm(request.POST)
            # if checkOutForm.is_valid():
            #     checkOutForm.save()
            #     return redirect('/app_Transaction/')
        else:
            checkOutForm = CheckOutForm()
            userData = getJSONofCurrentUser(request.session['polyCardData'])
            args = {'checkOutForm': checkOutForm,
                    'userFirstName': userData['first_Name']}
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


def studentLogin(request):
    if request.session.has_key('polyCardData'):
        return redirect('/app_Transaction/checkInOrCheckOut')
    else:
        if request.method == 'POST':
            checkPolyCardForm = studentLoginForm(request.POST)
            if checkPolyCardForm.is_valid():
                raw_PolyCard_Data = checkPolyCardForm.cleaned_data['polyCard_Data']
                polyCardData = getData(raw_PolyCard_Data)

                registeredStatus = None

                if polyCardData[1] == True:
                    all_Users = list(User.objects.all())

                    model_Attribute = 'polyCard_Data'

                    i = 0
                    while i < len(all_Users):
                        userInput = User.objects.values(model_Attribute)[
                            i][model_Attribute]

                        if userInput == raw_PolyCard_Data:
                            registeredStatus = True
                            break
                        i += 1
                    if registeredStatus == True:
                        validInput = True
                        # request.session['polyCardData'] = User.objects.get(polyCard_Data=raw_PolyCard_Data).__dict__['polyCard_Data'])
                        request.session['polyCardData'] = str(
                            raw_PolyCard_Data)
                        return HttpResponseRedirect('/app_Transaction/checkInOrCheckOut')
                    else:
                        validInput = True
                        return HttpResponseRedirect('/app_Transaction/registration')
                else:
                    return HttpResponseRedirect('/app_Transaction/')

        else:
            checkPolyCardForm = studentLoginForm()
            args = {'checkPolyCardForm': checkPolyCardForm}
            return render(request, 'app_Transaction/studentLogin.html', args)

        return render(request, 'app_Transaction/checkPolyCard.html')


def parts(request):
    all_Parts = list(Part.objects.all())
    i = 0
    registered_Parts_List = []

    total_Parts = len(all_Parts)
    while i < total_Parts:
        part = Part.objects.values('part')[i]['part']
        partQty = Part.objects.values('quantity')[i]['quantity']
        # partData = {"PartName": part, "PartQty": partQty}
        registered_Parts_inner = [part, partQty]
        registered_Parts_List.append(registered_Parts_inner)
        i += 1
    # registered_Parts_List = sorted(registered_Parts_List)
    args = {'registered_Parts_List': registered_Parts_List,
            'total_Parts': total_Parts}
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
    args = {'registered_Users_List': registered_Users_List,
            'total_Users': total_Users}
    return render(request, 'app_Transaction/registeredUsers.html', args)


def registration(request):
    if request.method == 'POST':
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

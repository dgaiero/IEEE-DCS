from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms
from pprint import pprint
from django.forms import ValidationError

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

    if request.session.has_key('CustomerPolyCardData'):
        if request.method == 'POST':
            partData = json.loads(request.POST["partData"])
            userData = User.objects.get(
                polyCard_Data=request.session['CustomerPolyCardData'])
            # print(partData)

            for key, value in partData.items():
                partData = value
                # pprint(partData)
                partName = value['partName']
                partID = value['partID']
                partQty = int(value['partQty'])
                # try:
                #     print("TRYPART")
                #     partQty = int(value['partQty'])
                #     partCheckedOut_qty = partCheckedOut.quantity_Checked_Out
                #     # partCheckedOut_qty = 1
                #     print(partCheckedOut_qty)
                #     # print(partCheckedOut_qty)
                # except ValueError:
                #     print("ValueError")
                #     pass
                try:
                    partCheckedOut = userPart.objects.get(
                        userAssigned=userData, part=partName, id_Number=partID)

                    if (int(partCheckedOut.quantity_Checked_Out) == partQty):
                        print("SAME QTY")
                        partCheckedOut.delete()
                    else:
                        print("DIFF QTY")
                        partCheckedOut.quantity_Checked_Out = int(partCheckedOut.quantity_Checked_Out)-partQty
                        partCheckedOut.save()
                except ObjectDoesNotExist:
                    pass

            return redirect('/app_Transaction/')

        else:
            userData = getJSONofCurrentUser(request.session['CustomerPolyCardData'])

            all_Parts = list(userPart.objects.filter(userAssigned=User.objects.get(
                polyCard_Data=request.session['CustomerPolyCardData'])))
            # print(all_Parts)

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
    else:
        return redirect('/app_Transaction/')


def studentLogout(request):
    try:
        del request.session['CustomerPolyCardData']
    except:
        print("Fail")
        pass
    args = {'logoutFlag': "True"}
    return redirect('/app_Transaction/studentLogin/?logoutFlag=True', args)
    # return HttpResponse("<strong>You are logged out.</strong>")


def checkIn_Or_CheckOut(request):
    if request.session.has_key('CustomerPolyCardData'):
        userData = getJSONofCurrentUser(request.session['CustomerPolyCardData'])

        args = {'userFirstName': userData['first_Name'],'userLastName': userData['last_Name'], 'memberType': userData['userType'], 'email': userData['cal_Poly_Email'], 'ieee_member_number': userData['ieee_member_number'], 'expireDate':userData['ieee_member_expiration_date'],'itemsCheckedOut': userData['has_Items_Checked_Out']}
        return render(request, 'app_Transaction/CheckInOrCheckOut.html', args)
    else:
        return redirect('/app_Transaction/')


def checkOut(request):
    if request.session.has_key('CustomerPolyCardData'):
        if request.method == 'POST':
            partData = json.loads(request.POST['partData'])
            userData = User.objects.get(
                polyCard_Data=request.session['CustomerPolyCardData'])
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
            userData = getJSONofCurrentUser(request.session['CustomerPolyCardData'])
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
    if request.session.has_key('CustomerPolyCardData'):
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
                        request.session['CustomerPolyCardData'] = str(
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
        registrationFormData = RegistrationForm(request.POST)
        if registrationFormData.is_valid():
            print(registrationFormData)
            registrationFormData.save()
            return redirect('/app_Transaction/')
        else:
            print (registrationFormData.errors)
            args = {'registrationForm': registrationFormData, 'errors': registrationFormData.errors}
            return render(request, 'app_Transaction/registration.html', args)
            # return redirect('/app_Transaction/registration/?fail=True', args)
    else:
        registrationForm = RegistrationForm()
        args = {'registrationForm': registrationForm}
        return render(request, 'app_Transaction/registration.html', args)


def transaction_Summary(request):
    if request.session.has_key('CustomerPolyCardData'):
        userData = getJSONofCurrentUser(request.session['CustomerPolyCardData'])
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

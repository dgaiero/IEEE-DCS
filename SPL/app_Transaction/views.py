from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms
from pprint import pprint
from django.forms import ValidationError

import json
import urllib.parse
from datetime import datetime

from .models import User, Part, userPart, eventLog
from .filters import UserFilter
from django.core.exceptions import ObjectDoesNotExist
from app_Transaction.forms import RegistrationForm, studentLoginForm, CheckOutForm
from app_Transaction.user_registration_scripts.polyCardData import getData

# import os
# os.environ['DJANGO_SETTINGS_MODULE']='SPL.settings'


# try to include error messages here
def getJSONofCurrentUser(sessionData):
    currentUserData = User.objects.get(cal_Poly_Email=sessionData).__dict__
    return currentUserData
# Define function-based views


def searchUser(request):
    if request.session.has_key('AdminPolyCardData'):
        user_list = User.objects.all()
        user_filter = UserFilter(request.GET, queryset=user_list)
        checkPolyCardData(request)
        userData = getJSONofCurrentUser(request.session['CustomerPolyCardData'])
        adminData = getJSONofCurrentUser(request.session['AdminPolyCardData'])
        return render(request, 'app_Transaction/search_user.html', {'filter': user_filter, 'userData': userData, 'adminData': adminData})
    else:
        return redirect('/app_Transaction/')


def logEventData(checkedOutTo, checkedOutBy, logType, content):
    newLogEvent = eventLog(checkedOutTo=checkedOutTo,
                           checkedOutBy=checkedOutBy, logType=logType, content=content)
    newLogEvent.save()


def another_Action(request):
    return render(request, 'app_Transaction/anotherAction.html')


def checkIn(request):

    if request.session.has_key('AdminPolyCardData'):
        if request.method == 'POST':
            partData = json.loads(request.POST["partData"])
            checkPolyCardData(request)
            userData = getJSONofCurrentUser(request.session['CustomerPolyCardData'])
            adminData = getJSONofCurrentUser(request.session['AdminPolyCardData'])
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
            checkPolyCardData(request)
            userData = getJSONofCurrentUser(request.session['CustomerPolyCardData'])
            adminData = getJSONofCurrentUser(request.session['AdminPolyCardData'])

            all_Parts = list(userPart.objects.filter(userAssigned=User.objects.get(
                cal_Poly_Email=request.session['CustomerPolyCardData'])))
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
                    'userData': userData, 'adminData': adminData}
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

def adminLogout(request):
    try:
        del request.session['AdminPolyCardData']
    except:
        print("Fail")
        pass
    args = {'logoutFlag': "True"}
    return redirect('/app_Transaction/studentLogin/?logoutFlag=True', args)

def checkPolyCardData(request):
    if request.session.has_key('AdminPolyCardData'):
        if not request.session.has_key('CustomerPolyCardData'):
            request.session['CustomerPolyCardData'] = getJSONofCurrentUser(request.session['AdminPolyCardData'])['polyCard_Data']

def checkIn_Or_CheckOut(request):
    if request.session.has_key('AdminPolyCardData') or request.session.has_key('CustomerPolyCardData'):
        checkPolyCardData(request)
        userData = getJSONofCurrentUser(request.session['CustomerPolyCardData'])
        updateUserData = userData
        updateUserData["polyCard_Data"] =  urllib.parse.quote(userData["polyCard_Data"], safe="")
        try:
            updateUserData["ieee_member_expiration_date"] = userData['ieee_member_expiration_date'].strftime('%m/%d/%Y')
        except AttributeError:
            pass
        try:
            adminData = getJSONofCurrentUser(request.session['AdminPolyCardData'])
            args = {'userData': userData, 'adminData': adminData}
        except KeyError:
            args = {'userData': updateUserData}
        return render(request, 'app_Transaction/CheckInOrCheckOut.html', args)
    else:
        return redirect('/app_Transaction/')


def checkOut(request):
    if request.session.has_key('AdminPolyCardData'):
        if request.method == 'POST':
            partData = json.loads(request.POST['partData'])
            userData = User.objects.get(
                cal_Poly_Email=request.session['CustomerPolyCardData'])
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
            checkPolyCardData(request)
            userData = getJSONofCurrentUser(request.session['CustomerPolyCardData'])
            adminData = getJSONofCurrentUser(request.session['AdminPolyCardData'])
            args = {'checkOutForm': checkOutForm,
                    'userData': userData, 'adminData': adminData}
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
    # if request.session.has_key('CustomerPolyCardData') or request.session.has_key('OfficerPolyCardData'):
    #     return redirect('/app_Transaction/checkInOrCheckOut')
    # else:
    if request.method == 'POST':
        checkPolyCardForm = studentLoginForm(request.POST)
        if checkPolyCardForm.is_valid():
            raw_PolyCard_Data = checkPolyCardForm.cleaned_data['polyCard_Data']
            try:
                currentUser = User.objects.get(polyCard_Data=raw_PolyCard_Data)
                loginStatus = loginUser(currentUser, request)
            except ObjectDoesNotExist:
                loginStatus = 2

            if loginStatus == 1:
                return HttpResponseRedirect('/app_Transaction/checkInOrCheckOut')
            if loginStatus == 2:
                polyCardData = urllib.parse.quote(raw_PolyCard_Data, safe="")
                return HttpResponseRedirect('/app_Transaction/registration/?polyCard_Data={}'.format(polyCardData))
        else:
            args = {'checkPolyCardForm': checkPolyCardForm, 'errors': checkPolyCardForm.errors}
            return render(request, 'app_Transaction/studentLogin.html', args)

    # elif request.method == 'GET':
    #     print("GET")
    #     return HttpResponse("Login as new user is not yet fully operational.")
    else:
        if request.session.has_key('AdminPolyCardData'):
            if 'mode' in request.GET:
                if request.GET['mode'] == 'passthrough':
                    print("testtest")
                    currentUser = User.objects.get(cal_Poly_Email=request.GET['email'])
                    loginUser(currentUser,request)

                    if 'service' in request.GET:

                        print(request.GET['service'])
                        return HttpResponseRedirect(request.GET['service'])
        else:
            pass
        checkPolyCardForm = studentLoginForm(initial=request.GET.dict())
        checkPolyCardData(request)
        args = {'checkPolyCardForm': checkPolyCardForm}
        # userData = getJSONofCurrentUser(request.session['CustomerPolyCardData'])
        # args['userData'] = userData
        try:
            userData = getJSONofCurrentUser(request.session['CustomerPolyCardData'])
            args['userData'] = userData
        except:
            print("No user data")
        try:
            adminData = getJSONofCurrentUser(request.session['AdminPolyCardData'])
            args['adminData'] = adminData
        except:
            print("No admin data")

        return render(request, 'app_Transaction/studentLogin.html', args)

    return render(request, 'app_Transaction/checkPolyCard.html')


def loginUser(currentUser, request):
    try:

        print(currentUser.userType)
        if currentUser.userType == 'ADMIN' or currentUser.userType == 'OFFICER':
            request.session['AdminPolyCardData'] = str(
                currentUser.cal_Poly_Email)
        if request.session.has_key('CustomerPolyCardData'):
            try:
                if getJSONofCurrentUser(request.session['CustomerPolyCardData'])['userType'] == 'ADMIN' or \
                        getJSONofCurrentUser(request.session['CustomerPolyCardData'])['userType'] == 'OFFICER':
                    request.session['CustomerPolyCardData'] = str(currentUser.cal_Poly_Email)
            except:
                pass
        else:
            request.session['CustomerPolyCardData'] = str(currentUser.cal_Poly_Email)
        return 1
    except ObjectDoesNotExist:
        return 2


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
    if request.session.has_key('AdminPolyCardData'):
        if request.method == 'POST':
            registrationFormData = RegistrationForm(request.POST)
            if registrationFormData.is_valid():
                print(registrationFormData.cleaned_data['mode'])
                if registrationFormData['mode'] == "create":
                    print(registrationFormData)
                    registrationFormData.save()
                    return redirect('/app_Transaction/')
                else:
                    userToUpdate = User.objects.get(cal_Poly_Email=getJSONofCurrentUser(request.session['CustomerPolyCardData'])["cal_Poly_Email"])
                    userToUpdate.first_Name=registrationFormData.cleaned_data['first_Name']
                    userToUpdate.last_Name=registrationFormData.cleaned_data['last_Name']
                    userToUpdate.cal_Poly_Email=registrationFormData.cleaned_data['cal_Poly_Email']
                    userToUpdate.ieee_member_number=registrationFormData.cleaned_data['ieee_member_number']
                    userToUpdate.ieee_member_expiration_date=registrationFormData.cleaned_data['ieee_member_expiration_date']
                    userToUpdate.phone_Number=registrationFormData.cleaned_data['phone_Number']
                    userToUpdate.polyCard_Data=registrationFormData.cleaned_data['polyCard_Data']
                    userToUpdate.user_Type=registrationFormData.cleaned_data['userType']
                    userToUpdate.save()

                    return redirect('/app_Transaction/')
            else:
                print (registrationFormData.errors)
                args = {'registrationForm': registrationFormData, 'errors': registrationFormData.errors}
                return render(request, 'app_Transaction/registration.html', args)
                # return redirect('/app_Transaction/registration/?fail=True', args)
        else:
            registrationForm = RegistrationForm(initial=request.GET.dict())
            checkPolyCardData(request)
            userData = getJSONofCurrentUser(request.session['CustomerPolyCardData'])
            adminData = getJSONofCurrentUser(request.session['AdminPolyCardData'])
            args = {'registrationForm': registrationForm, 'userData':userData, 'adminData':adminData}
            return render(request, 'app_Transaction/registration.html', args)
    else:
        return redirect('/app_Transaction/')


def transaction_Summary(request):
    if request.session.has_key('CustomerPolyCardData'):
        userData = getJSONofCurrentUser(request.session['CustomerPolyCardData'])
        return render(request, 'app_Transaction/transactionSummary.html')
    else:
        return redirect('/app_Transaction/')

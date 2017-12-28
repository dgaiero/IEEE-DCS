from django import forms
from django.db import models

# Import user model here
from .models import User
#from phonenumber_field.modelfields import PhoneNumberField
from app_Transaction.user_registration_scripts.polyCardData import getData
from app_Transaction.models import User


class CheckPolyCardForm(forms.ModelForm):
    polyCard_Data = forms.CharField(required=True)

    #polycardData = getData(polyCard_Data)
    #print(polycardData)

    class Meta:
        model = User
        fields = ('polyCard_Data',)

    def save(self, commit=True):
        user = super(CheckPolyCardForm, self).save(commit=False)
        user.polyCardData = self.cleaned_data['polyCard_Data']
        polyCardData = getData(user.polyCardData)

        '''
        if (polyCardData is not(None)):
            ## This might need some fixing...
            isoNumber = user.polyCardData['iso_Number']
            libraryCodeNumber = user.polyCardData['libraryCodeNumber']
            ## End fixing...
        '''
        registeredStatus = None
        validInput = None

        if polyCardData[1] == True:
            all_Users = list(User.objects.all())

            model_Attribute = 'polyCard_Data'

            i = 0
            while i < len(all_Users):
                userInput = User.objects.values(model_Attribute)[i][model_Attribute]
                if userInput == user.polyCardData:
                    print ('\nYou are already registered!\n')
                    registeredStatus = True
                    break
                i += 1

            if registeredStatus == True:
                print ('\nYou will be redirected to checkInOrCheckOut page\n')
                validInput = True
                return (validInput, registeredStatus)
                # redirect to checkInOrCheckOut page
            else:
                print ('\nYou will be redirected to register page\n')
                validInput = True
                return (validInput, registeredStatus)
        else:
            print ('\nInvalid PolyCard! Please swipe a valid PolyCard\n')
            validInput = False
            return (validInput, registeredStatus)

        '''
        Pseudo code for next steps:

        #1 if get data returns useful info:
            check if polyCardData is in user database
             #2 if iso is in database:
                redirect user to checkin or check out page
             #3 else:
                redirect user to register page
                # Add dom stuff here
        #4 else:
            tell user invalid polycard and redirect them back to checkPolyCard page
            client validation here
        '''
        #pass


class RegistrationForm(forms.ModelForm):
    first_Name = forms.CharField(required=True)
    last_Name = forms.CharField(required=True)
    # see if you can force @calpoly.edu on email field
    cal_Poly_Email = forms.EmailField(required=True)
    phone_Number = forms.IntegerField(
        required=True, help_text='(e.g. 8057561111)')
    # user_Phone_Number = PhoneNumberField()

    class Meta:
        model = User
        fields = (
            'first_Name',
            'last_Name',
            'cal_Poly_Email',
            'phone_Number',
        )

    # Create a function that saves data to the model
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_Name = self.cleaned_data['first_Name']
        user.last_Name_Text = self.cleaned_data['last_Name']
        user.user_Email = self.cleaned_data['cal_Poly_Email']
        user.user_Phone_Number = self.cleaned_data['phone_Number']

        if commit:
            user.save()

        return User

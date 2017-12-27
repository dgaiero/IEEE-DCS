from django import forms
#from django.db import models

# Import user model here
from .models import User
#from phonenumber_field.modelfields import PhoneNumberField
from app_Transaction.user_registration_scripts.polyCardData import getData


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
        polycardData = getData(user.polyCardData)
        print(polycardData)
        '''
        if get data returns useful info:
            check if iso number is in user database

            if iso is in database:
                redirect user to checkin or check out page
            else:
                redirect user to register page
        else:
            tell user invalid polycard and redirect them back to checkPolyCard page
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

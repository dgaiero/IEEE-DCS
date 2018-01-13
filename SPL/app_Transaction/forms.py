from django import forms
from django.db import models

# Import custom scripts here
from .models import User, Part
#from phonenumber_field.modelfields import PhoneNumberField
from app_Transaction.user_registration_scripts.polyCardData import getData
from app_Transaction.models import User

# Define class-based model forms

all_Parts = list(Part.objects.all())
i = 0
PART_CHOICES = []
registered_Parts_List = []
total_Parts = len(all_Parts)
while i < total_Parts:
    part = Part.objects.values('part')[i]['part']
    PART_CHOICES.append(('{}'.format(part), '{}'.format(part)))
    i += 1

PART_CHOICES = sorted(PART_CHOICES)

QUANTITY_CHOICES = []
j = 1
max_length = 101
while j < max_length:
    QUANTITY_CHOICES.append(('{}'.format(j), '{}'.format(j)))
    j += 1


class CheckOutForm(forms.ModelForm):
    part = forms.CharField(widget=forms.Select(
        choices=PART_CHOICES, attrs={'class': 'form-control', 'id': 'partName'}))
    quantity = forms.IntegerField(
        widget=forms.Select(choices=QUANTITY_CHOICES, attrs={'class': 'form-control', 'id': 'partQty'}))
    id_Number = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'partID'}))

    class Meta:
        model = Part
        fields = ('part',
                  'quantity',
                  'quantity_Checked_Out',
                  'id_Number',)
        exclude = ('quantity_Checked_Out',)


class CheckPolyCardForm(forms.ModelForm):
    polyCard_Data = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('polyCard_Data',)


class RegistrationForm(forms.ModelForm):
    first_Name = forms.CharField(required=True)
    last_Name = forms.CharField(required=True)
    polyCard_Data = forms.CharField(required=True)
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
            'polyCard_Data',
            'cal_Poly_Email',
            'phone_Number',
            'iso_Number',
            'library_Code_Number',
        )
        exclude = ('iso_Number', 'library_Code_Number',)

    # Create a function that saves data to the model
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_Name = self.cleaned_data['first_Name']
        user.last_Name = self.cleaned_data['last_Name']
        user.polyCard_Data = self.cleaned_data['polyCard_Data']

        raw_PolyCard_Data = user.polyCard_Data
        polyCardData = getData(raw_PolyCard_Data)
        library_Code_Number = polyCardData[0]['libraryCodeNumber']
        iso_Number = polyCardData[0]['isoNumber']

        user.library_Code_Number = library_Code_Number
        user.iso_Number = iso_Number
        user.user_Email = self.cleaned_data['cal_Poly_Email']
        user.user_Phone_Number = self.cleaned_data['phone_Number']

        if commit:
            user.save()

        return User

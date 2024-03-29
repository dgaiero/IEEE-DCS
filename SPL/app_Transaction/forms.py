from django import forms

# from phonenumber_field.modelfields import PhoneNumberField
from app_Transaction.models import User
# Import custom scripts here
from .models import Part
from .validators import validate_polyCard


# Define class-based model forms

# all_Parts = list(Part.objects.all())
# i = 0
# PART_CHOICES = []
# registered_Parts_List = []
# total_Parts = len(all_Parts)
# while i < total_Parts:
#     part = Part.objects.values('part')[i]['part']
#     PART_CHOICES.append(('{}'.format(part), '{}'.format(part)))
#     i += 1
#
# PART_CHOICES = sorted(PART_CHOICES)
#
# QUANTITY_CHOICES = []
# j = 1
# max_length = 101
# while j < max_length:
#     QUANTITY_CHOICES.append(('{}'.format(j), '{}'.format(j)))
#     j += 1


class CheckOutForm(forms.ModelForm):
    part = forms.CharField(widget=forms.Select(
        choices=("test","test"), attrs={'class': 'form-control', 'id': 'partName'}))
    quantity = forms.IntegerField(
        widget=forms.Select(choices=("test","test"), attrs={'class': 'form-control', 'id': 'partQty'}))
    id_Number = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'partID'}))

    class Meta:
        model = Part
        fields = ('part',
                  'quantity',
                  'quantity_Checked_Out',
                  'id_Number',)
        exclude = ('quantity_Checked_Out',)


class studentLoginForm(forms.ModelForm):
    polyCard_Data = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg polyCardDataFieldMask', 'id': 'polycardPasswordInput'}))

    class Meta:
        model = User
        fields = ('polyCard_Data',)


class messageForm(forms.Form):
    users_to = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    users_from_email = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    users_from_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))

class RegistrationForm(forms.ModelForm):
    mode = forms.CharField(required=False, initial="create")
    first_Name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_Name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    polyCard_Data = forms.CharField(required=False,
                                    widget=forms.TextInput(attrs={'class': 'form-control polyCardDataFieldMask'}),
                                    validators=[validate_polyCard])
    # see if you can force @calpoly.edu on email field
    cal_Poly_Email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_Number = forms.CharField(required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'partName'}))
    ieee_member_number = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ieee_member_expiration_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'mm/dd/yyyy'}))
    # userType = forms.CharField(widget=forms.Select(
    #     choices=User.MEMBER_TYPE, attrs={'class': 'form-control'}))
    # user_Phone_Number = PhoneNumberField()



    class Meta:
        model = User
        fields = (
            'first_Name',
            'last_Name',
            'polyCard_Data',
            'cal_Poly_Email',
            'phone_Number',
            'ieee_member_number',
            'ieee_member_expiration_date',
            # 'userType'
        )
        exclude = ('iso_Number', 'library_Code_Number',)

    # Create a function that saves data to the model
    # def save(self, commit=True):
    #     user = super(RegistrationForm, self).save(commit=False)
    #     user.first_Name = self.cleaned_data['first_Name']
    #     user.last_Name = self.cleaned_data['last_Name']
    #     user.polyCard_Data = self.cleaned_data['polyCard_Data']
    #
    #     raw_PolyCard_Data = user.polyCard_Data
    #     polyCardData = getData(raw_PolyCard_Data)
    #     library_Code_Number = polyCardData[0]['libraryCodeNumber']
    #     iso_Number = polyCardData[0]['isoNumber']
    #
    #     user.library_Code_Number = library_Code_Number
    #     user.iso_Number = iso_Number
    #     user.user_Email = self.cleaned_data['cal_Poly_Email']
    #     user.user_Phone_Number = self.cleaned_data['phone_Number']
    #
    #     if commit:
    #         user.save()
    #
    #     return User

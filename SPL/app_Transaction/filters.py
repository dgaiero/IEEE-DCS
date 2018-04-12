import django_filters

from .models import User


class UserFilter(django_filters.FilterSet):
    # first_Name = django_filters.CharFilter(lookup_expr='icontains')
    # last_Name = django_filters.CharFilter(lookup_expr='icontains')
    cal_Poly_Email = django_filters.CharFilter(lookup_expr='icontains')
    ieee_member_expiration_date = django_filters.NumberFilter(name='ieee_member_expiration_date', lookup_expr='year')

    class Meta:
        model = User
        fields = {
            'first_Name': ['exact', 'icontains'],
            'last_Name': ['exact', 'icontains'],
            'userType': ['exact'],
            'cal_Poly_Email': ['icontains'],
            'ieee_member_number': ['exact', 'icontains'],
            'ieee_member_expiration_date': ['year'],
            'phone_Number': ['exact', 'icontains'],
            'polyCard_Data': ['exact'],
        }
        # fields = ['first_Name', 'last_Name', 'userType', 'cal_Poly_Email', 'ieee_member_number',
        #           'ieee_member_expiration_date', 'phone_Number', 'polyCard_Data']

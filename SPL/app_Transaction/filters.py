from .models import User
import django_filters

class UserFilter(django_filters.FilterSet):

    first_Name = django_filters.CharFilter(lookup_expr='icontains')
    last_Name = django_filters.CharFilter(lookup_expr='icontains')
    cal_Poly_Email = django_filters.CharFilter(lookup_expr='icontains')
    year_expired = django_filters.NumberFilter(name='ieee_member_expiration_date', lookup_expr='year')

    class Meta:
        model = User
        fields = ['first_Name','last_Name','cal_Poly_Email','ieee_member_number','ieee_member_expiration_date','phone_Number','polyCard_Data']

from django.contrib import admin

# Register and make models modifiable in the admin
from .models import Part, User

# Create visual settings for Part class in Django admin
class PartAdmin(admin.ModelAdmin):
    list_display  = ('part',
                     'quantity',
                     'quantity_Checked_Out',
                     'id_Number',)
    list_filter   = ['part',]
    search_fields = ['part',
                    'id_Number',]

# Create visual settings for User class in Django admin
class UserAdmin(admin.ModelAdmin):
    list_display  = ('first_Name',
                     'last_Name',
                     'cal_Poly_Email',
                     'phone_Number',)
    list_filter   = ['first_Name',
                     'last_Name',
                     'cal_Poly_Email',]
    search_fields = ['first_Name',
                     'last_Name',
                     'cal_Poly_Email',
                     'phone_Number']

# Register classes with the Django admin
# register() takes 2-3 arguments at one time
admin.site.register(User, UserAdmin)
admin.site.register(Part, PartAdmin)

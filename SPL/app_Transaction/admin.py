from django.contrib import admin

# Register and make models modifiable in the admin
from .models import Part, User

# Create visual settings for Part class in Django admin
class PartAdmin(admin.ModelAdmin):
    list_display  = ('part_Name_Text',
                     'quantity_Number',
                     'quantity_Checked_Out_Number',
                     'id_Number',)
    list_filter   = ['part_Name_Text',]
    search_fields = ['part_Name_Text',
                    'id_Number',]

# Create visual settings for User class in Django admin
class UserAdmin(admin.ModelAdmin):
    list_display  = ('first_Name_Text',
                     'last_Name_Text',
                     'user_Email',)
    list_filter   = ['first_Name_Text',
                     'last_Name_Text',
                     'user_Email',]
    search_fields = ['first_Name_Text',
                     'last_Name_Text',
                     'user_Email',]

# Register classes with the Django admin
# register() takes 2-3 arguments at one time
admin.site.register(User, UserAdmin)
admin.site.register(Part, PartAdmin)

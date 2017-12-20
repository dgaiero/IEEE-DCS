from django.contrib import admin

# Register your models here.
# Here we are making the PolyCardData modifiable in the admin
from .models import PolyCard, Part

class PartAdmin(admin.ModelAdmin):
    list_display = ('part_Name_Text', 'quantity_Number', 'quantity_Checked_Out_Number', 'id_Number')
    list_filter = ['part_Name_Text']
    search_fields = ['part_Name_Text', 'id_Number']
admin.site.register(PolyCard)
admin.site.register(Part, PartAdmin)

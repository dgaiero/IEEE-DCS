from django.contrib import admin

# Register your models here.
# Here we are making the PolyCardData modifiable in the admin
from .models import PolyCard, Part

admin.site.register(PolyCard)
admin.site.register(Part)

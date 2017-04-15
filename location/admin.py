from django.contrib import admin
from .models import Places

class PlaceAdmin(admin.ModelAdmin):
	list_display = ('title', 'location')

admin.site.register(Places, PlaceAdmin)



# Register your models here.

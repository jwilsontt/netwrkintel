from django.contrib import admin
from .models import ISPointCodes
from isocc.models import CountryIso

# Register your models here.

class ISPCAdmin(admin.ModelAdmin):
	list_display = ('ispc', 'dec', 'sigpoint_name', 'sigpoint_operator', 'sigpoint_country')
	list_filter = ['sigpoint_country']

	def ispc(self, obj):
		return obj.ispc

admin.site.register(ISPointCodes, ISPCAdmin)
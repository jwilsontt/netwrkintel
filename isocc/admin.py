from django.contrib import admin
from .models import CountryIso
# Register your models here.

class CountryAdmin(admin.ModelAdmin):
	list_display = ('country_name', 'alpha_2', 'alpha_3')
	search_fields = ['country_name']

	def country_name(self, obj):
		return obj.country_name

	country_name.admin_order_field = 'country_name'

admin.site.register(CountryIso, CountryAdmin)
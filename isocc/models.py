from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

class CountryIso(models.Model):
	country_name = models.CharField(max_length=200)
	alpha_2 = models.CharField(max_length=2)
	alpha_3 = models.CharField(max_length=3)
	un_m49_num = models.IntegerField(default=0)

	def __str__(self):
		return self.country_name		
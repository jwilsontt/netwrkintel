from django.db import models
from isocc.models import CountryIso

# Create your models here.

class ISPointCodes(models.Model):
	ispc = models.CharField(max_length=12)
	dec = models.IntegerField()
	sigpoint_name = models.CharField(max_length=100)
	sigpoint_operator = models.CharField(max_length=250)
	sigpoint_country = models.ForeignKey('isocc.CountryIso', on_delete=models.CASCADE)

	def __str__(self):
		return self.ispc
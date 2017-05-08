from django.db import models
from isocc.models import CountryIso

# Create your models here.

class ISPointCodes(models.Model):
	ispc = models.CharField(max_length=12)
	dec = models.IntegerField(default=1)
	sigpoint_name = models.CharField(null=True, blank=True, max_length=100)
	sigpoint_operator = models.CharField(max_length=250)
	sigpoint_country = models.ForeignKey('isocc.CountryIso', on_delete=models.CASCADE)

	class Meta:
		ordering = ["ispc"]

	def __str__(self):
		return self.ispc
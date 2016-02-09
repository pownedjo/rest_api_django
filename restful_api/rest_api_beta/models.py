from __future__ import unicode_literals
from django.db import models



## Django gives automaticaly a Primary key for each Model
class User(models.Model):
	user_first_name = models.CharField(max_length=30)
	user_last_name = models.CharField(max_length=30)
	user_age = models.PositiveSmallIntegerField()
	user_sexe = models.CharField(max_length=10)
	user_email = models.EmailField(max_length=75)
	user_tel = models.CharField(max_length=30)
	

## Clef etrangere User -> Urgence (many to one)
## Priority urgence : 0 < _ < 100
class Urgence(models.Model):
	urgence_user = models.ForeignKey(User, verbose_name="related user")
	urgence_priority = models.PositiveIntegerField()
	urgence_reason = models.CharField(max_length=100)
	urgence_lattitude = models.DecimalField(max_digits=5, decimal_places=4)
	urgence_longitude = models.DecimalField(max_digits=5, decimal_places=4)
	urgence_altitude = models.DecimalField(max_digits=6, decimal_places=2)
	

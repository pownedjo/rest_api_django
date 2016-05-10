from __future__ import unicode_literals
from django.db import models

##EMERGENCY_STATUS = (
##    ('ok', 'processed'),
##    ('in', 'in progress'),
##    ('nok', 'not started'),
##)

## Django gives automaticaly a Primary key for each Model
class User(models.Model):
	user_first_name = models.CharField("prenom", max_length=30, null=True)
	user_last_name = models.CharField("nom de famille", max_length=30, null=True)
	user_age = models.PositiveSmallIntegerField("age", null=True)
	user_sexe = models.CharField("sexe", max_length=10, null=True)
	user_email = models.EmailField("mail", max_length=75, unique=True, null=True)
	user_tel = models.CharField("Telephone", max_length=30, unique=True, null=True, blank=True)
	user_registration_date = models.DateTimeField("Date enregistrement", auto_now_add=True)

	## Drop down list name display
	def __unicode__(self):
		return 'User : ' + self.user_tel



## Clef etrangere User -> Urgence (many to one)
## Priority urgence : 0 < _ < 100
class Urgence(models.Model):
	urgence_user = models.ForeignKey(User, verbose_name="utilisateur urgence", null=True, blank=True)
	urgence_priority = models.PositiveIntegerField("priorite", null=True)
	urgence_reason = models.CharField("motif", max_length=100, null=True)
	urgence_lattitude = models.DecimalField("lattitude", max_digits=9, decimal_places=7, null=True)
	urgence_longitude = models.DecimalField("longitude", max_digits=9, decimal_places=7, null=True)
	urgence_altitude = models.DecimalField("altitude", max_digits=11, decimal_places=7, null=True)
	urgence_speed = models.DecimalField("vitesse", max_digits=10, decimal_places=7, null=True)
	urgence_timestamp = models.DateTimeField("urgence timestamp", auto_now_add=True)
	#urgence_status = models.CharField("statut" , max_length=15, choices=EMERGENCY_STATUS, null=True)

	### coerce_to_string = True : return Decimal in String format

	def __unicode__(self):
		try :
			return 'Urgence : ' + str(self.urgence_timestamp)
		except Exception, e :
			return "Error:%s" % str(e)

	def user_infos(self):
		try:
			return "" + self.urgence_user.user_first_name + " - " + self.urgence_user.user_last_name
		except Exception, e :
			return "Error:%s" % str(e)

	def user_telephone(self):
		try:
			return "" + self.urgence_user.user_tel
		except Exception, e :
			return "Error:%s" % str(e)



class Vehicle(models.Model):
	vehicle_user = models.ForeignKey(User, verbose_name="utilisateur vehicle", null=True, blank=True)
	vehicle_brand = models.CharField("Marque Vehicule", max_length=50, null=True, blank=True)
	vehicle_model = models.CharField("Model Vehicule", max_length=50, null=True, blank=True)
	vehicle_color = models.CharField("Couleur Vehicule", max_length=50, null=True, blank=True)
	vehicle_license_plate = models.CharField("Immatriculation Vehicule", max_length=50, null=True, blank=True)



class ImageFileUrgence(models.Model):
	id_urgence = models.ForeignKey(Urgence, verbose_name="urgence", null=True, blank=True)
	photo_file = models.ImageField()
	comment_photo_file = models.CharField("Commentaires photo", max_length=300, null=True, blank=True)



### DEFINE MODEL FOR BLE/WIFI/ETC... LOCATION AND ADDITIONAL INFOS ###
class DeviceAndPlace(models.Model):
	device_user = models.ForeignKey(User, verbose_name="utilisateur device", null=True, blank=True)
	device_comment = models.CharField("Commentaires device", max_length=300, null=True, blank=True)
	#device_position = models.

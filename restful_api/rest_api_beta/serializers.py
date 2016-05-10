from rest_api_beta.models import User
from rest_api_beta.models import Urgence
from rest_api_beta.models import ImageFileUrgence
from rest_api_beta.models import Vehicle
from rest_framework import serializers



class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'user_registration_date', 'user_first_name', 'user_last_name', 'user_tel', 'user_age', 'user_sexe'
		, 'user_email')



class UrgenceSerializer(serializers.HyperlinkedModelSerializer):
	urgence_user = UserSerializer(required=False)

	class Meta:
		model = Urgence
		fields = ('urgence_user', 'id', 'urgence_priority', 'urgence_reason',
		'urgence_lattitude', 'urgence_longitude', 'urgence_altitude', 'urgence_speed')



class VehicleSerializer(serializers.HyperlinkedModelSerializer):
	vehicle_user = UserSerializer(required=False)

	class Meta:
		model = Vehicle
		fields = ('vehicle_user','vehicle_brand', 'vehicle_model', 'vehicle_color', 'vehicle_license_plate')



class ImageFileUrgenceSerializer(serializers.HyperlinkedModelSerializer):
	id_urgence = UrgenceSerializer(required=False)

	class Meta:
		model = ImageFileUrgence

		## FIchier Uploades : MEDIA_ROOT - settings.py
		fields = ('id_urgence', 'photo_file', 'comment_photo_file')



class UserAuthentificationSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = User
		fields = ('id', 'user_tel')

from rest_api_beta.models import User
from rest_api_beta.models import Urgence
from rest_framework import serializers



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('user_first_name', 'user_last_name', 'user_age', 'user_sexe'
		, 'user_email', 'user_tel')



class UrgenceSerializer(serializers.HyperlinkedModelSerializer):
	urgence_user = UserSerializer()
	
	class Meta:
		model = Urgence
		fields = ('urgence_user', 'urgence_priority', 'urgence_reason', 
		'urgence_lattitude', 'urgence_longitude', 'urgence_altitude')
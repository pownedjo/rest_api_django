from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_api_beta.models import User
from rest_api_beta.models import Urgence
from rest_api_beta.models import Vehicle
from rest_api_beta.models import ImageFileUrgence
from rest_api_beta.serializers import UserSerializer
from rest_api_beta.serializers import UrgenceSerializer
from rest_api_beta.serializers import VehicleSerializer
from rest_api_beta.serializers import ImageFileUrgenceSerializer



### LIST ALL USERS ###
@api_view(['GET'])
def users_list(request):
	if request.method == 'GET':
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)



### LIST ALL EMERGENCIES ###
@api_view(['GET'])
def urgences_list(request):
	if request.method == 'GET':
		urgences = Urgence.objects.all()
		serializer = UrgenceSerializer(urgences, many=True)
		return Response(serializer.data)



### URGENCE POST QUERRY ###
@api_view(['POST'])
def post_create_urgence(request, id_user, priority, reason, lattitude, longitude, altitude):

	#print 'DATAS = ' + str(request.data)

	try:
		user_object = User.objects.get(id=id_user)
	except User.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	print 'User in emergency situation = ' + str(user_object.user_first_name)

	if request.method == 'POST':
		serializer = UrgenceSerializer(data=request.data)

		if serializer.is_valid():
			emergency_situation = Urgence(urgence_user = user_object, urgence_priority = priority, urgence_reason = reason, urgence_altitude = altitude, urgence_lattitude = lattitude, urgence_longitude = longitude)
			emergency_situation.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



### URGENCE PUT QUERRY ###
#@api_view(['PUT'])
#def put_modify_urgence(request, ):



## GET URGENCE WITH UNIQUE ID ##
@api_view(['GET'])
def urgence_infos(request, id_emergency):
	try:
		emergency_object = Urgence.objects.get(id=id_emergency)
	except Urgence.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	serializer = UrgenceSerializer(emergency_object)
	return Response(serializer.data)



### USER TOKEN AUTHENTIFICATION [POST] ###
def user_auth(request):
	if request.method == 'POST':
		print hello
		ringo = User.objects.create(user_first_name = "ringo")
		ringo.save()



@api_view(['POST'])
def user_post_datas(request, user_phone, format=None):

	if request.method == 'POST':
		serializer = UserSerializer(data=request.data)

		if serializer.is_valid():
			u = User(user_first_name = user_phone)
			u.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def send_photos_urgence(request, comment_urgence):

	#try:
	#	urgence_object = Urgence.objects.get(id=id_urgence)
	#except Urgence.DoesNotExist:
	#	return Response(status=status.HTTP_404_NOT_FOUND)

	print 'Comment = ' + comment_urgence

	if request.method == "POST":
		serializer = ImageFileUrgenceSerializer(data=request.data)
		print 'Serial test'

		if serializer.is_valid():
			print 'Serial valid'
			image_field_urgence = ImageFileUrgence()
			image_field.comment_photo_file = form.cleaned_data["comment"]
 			image_field.photo = form.validated_data["photo"]
			image_field.id_urgence = form.cleaned_data["photo"]
			image_field.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #return render(request, 'contact.html', locals())



### HANDLE USER GET/POST/PUT/DELETE QUERRIES ###
@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def user_infos(request, id_user):

	try:
		user_object = User.objects.get(id=id_user)
	except User.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	## GET ##
	if request.method == 'GET':
		serializer = UserSerializer(user_object)
		return Response(serializer.data)

	## PUT ##
	elif request.method == 'PUT':
		serializer = UserSerializer(user_object, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	## POST ##
	elif request.method == 'POST':
		serializer = UrgenceSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	## DELETE ##
	elif request.method == 'DELETE':
		user_object.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

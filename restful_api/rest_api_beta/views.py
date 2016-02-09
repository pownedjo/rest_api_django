from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_api_beta.models import User
from rest_api_beta.models import Urgence
from rest_api_beta.serializers import UserSerializer
from rest_api_beta.serializers import UrgenceSerializer


@api_view(['GET'])
def users_list(request):
	if request.method == 'GET':
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)
		


@api_view(['GET'])
def urgences_list(request):
	if request.method == 'GET':
		urgences = Urgence.objects.all()
		serializer = UrgenceSerializer(urgences, many=True)
		return Response(serializer.data)
		

@api_view(['GET', 'PUT', 'DELETE'])
def user_infos(request, pk):
	
	try:
		user_object = User.objects.get(pk=pk)
	except User.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)


	if request.method == 'GET':
		serializer = UserSerializer(user_object)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = UserSerializer(snippet, data=request.data)
		
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	elif request.method == 'DELETE':
		user_object.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
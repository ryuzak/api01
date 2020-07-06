from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status

from django.shortcuts import get_object_or_404

from .serializers import UserSerializer
from .models import User

class RetrieveActiveUserAPIView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request):
		serializer = UserSerializer(request.user)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request):
		data = request.data
		serializer = UserSerializer(instance=request.user, data=data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_200_OK)

class CreateUserAPIView(APIView):
	permission_classes = (IsAuthenticated, )

	def post(self, request):
		data = request.data
		serializer = UserSerializer(data=data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)

class RetrieveUserAPIView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request, user_id):
		user = get_object_or_404(User, pk=user_id)
		serializer = UserSerializer(user)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, user_id):
		user = get_object_or_404(User, pk=user_id)
		data = request.data
		serializer = UserSerializer(instance=user, data=data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_200_OK)
	
	def delete(self, request, user_id):
		user = get_object_or_404(User, pk=user_id)
		user.is_active = False
		user.save()
		return Response({'message':'Usuario eliminado'}, status=status.HTTP_200_OK)

class RetreiveUsersAPIView(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request):
		users = User.objects.filter(is_active=True)
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


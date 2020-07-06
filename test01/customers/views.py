from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import status

from .serializers import CustomerSerializer
from accounts.serializers import UserSerializer

from .models import Customer

class CreateCustomerAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        data = request.data
        user_serializer = UserSerializer(data=data, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        serializer = CustomerSerializer(data=data, partial=True)
        serializer.data['user'] = user_serializer.data
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ListCustomersAPIView(APIView):
    Permission_classes = (IsAuthenticated, )

    def get(self, request):
        data = Customer.objects.filter(user__is_active=True)
        serializer = CustomerSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
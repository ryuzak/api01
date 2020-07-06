from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from .models import Marca
from .serializers import BrandSerializer
# Create your views here.

class BrandListAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        brand_list = Marca.objects.all()
        serializer = BrandSerializer(brand_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BrandCreateAPIView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        data = request.data
        serializer = BrandSerializer(data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
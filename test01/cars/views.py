from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from .models import Car
from .serializers import CarSerializer, CarOwnerSerializer

class RetrieveCarsAPIView(APIView):
	class_permissions = (AllowAny,)

	def get(self, request):
		'''
			Vista que regresa listado de autos
		'''
		cars = Car.objects.filter(status=True)
		serializer = CarSerializer(cars, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

class CreateCarAPIView(APIView):
	class_permissions = (AllowAny,)

	def post(self, request):
		car_obj = request.data
		serializer = CarSerializer(data=car_obj)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)


class RetrieveUpdateCarAPIView(APIView):
	class_permissions = (AllowAny,)

	def get(self, request, car_id):
		try:
			car_obj = Car.objects.get(pk=car_id)
		except Exception as e:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = CarSerializer(car_obj)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, car_id):
		car_data = request.data.get('car', {})
		try:
			car_obj = Car.objects.get(pk=car_id)
		except Exception as e:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = CarSerializer(instance=car_obj, data=car_data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_200_OK)

	def delete(self, request, car_id):
		try:
			car_obj = Car.objects.get(pk=car_id)
		except Exception as e:
			return Response(status=status.HTTP_404_NOT_FOUND)
		car_obj.status = False
		car_obj.save()
		serializer = CarSerializer(car_obj)
		return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

class AssingCarOwnerAPIView(APIView):
	permission_classes = (IsAuthenticated, )

	def post(self, request):
		data = request.data
		serializer = CarOwnerSerializer(data=data)
		serializer.is_valid(raise_exception=True)
		print(serializer.data['car'])
		print(dir(serializer))
		car = Car.objects.get(pk=serializer.data['car'])
		car.owner.add(serializer.data['owner'])
		car.save()
		return Response({'status':'ok', 'message':'Agregado ok'}, status=status.HTTP_200_OK)
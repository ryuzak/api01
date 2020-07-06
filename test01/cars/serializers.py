from rest_framework import serializers

from .models import Car

from marcas.serializers import BrandSerializer
from accounts.serializers import UserSerializer

class CarSerializer(serializers.ModelSerializer):
	owner = UserSerializer(many=True, read_only=True)
	class Meta:
		model = Car
		fields = ('id', 'name', 'year', 'color', 'fuel', 'status', 'brand', 'owner')

	def to_representation(self, instance):
		response = super().to_representation(instance)
		response['brand'] = BrandSerializer(instance.brand).data
		return response

class CarOwnerSerializer(serializers.Serializer):

	owner = serializers.IntegerField()
	car = serializers.IntegerField()
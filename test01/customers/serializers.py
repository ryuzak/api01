from rest_framework import serializers
from accounts.serializers import UserBasicSerializer
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserBasicSerializer(instance.user).data
        return response
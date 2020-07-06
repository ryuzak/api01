from rest_framework import serializers

from .models import Marca

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'
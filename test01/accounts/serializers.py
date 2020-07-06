from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
	date_joined = serializers.ReadOnlyField()
	
	class Meta:
		model = User
		fields = (
			'id', 
			'email', 
			'password', 
			'first_name', 
			'last_name', 
			'phone', 
			'date_joined', 
			'is_active',
		)
		extra_kwargs = {'password':{'write_only':True}}

	def update(self, instance, validated_data):
		instance.first_name = validated_data.get('first_name', instance.first_name)
		instance.last_name = validated_data.get('last_name', instance.last_name)
		instance.phone = validated_data.get('phone', instance.phone)
		instance.is_active = True
		instance.save()
		print(instance.__dict__)
		return instance

class UserBasicSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'first_name', 'email')
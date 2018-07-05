from rest_framework import serializers
from . models import weather

class weatherSerializer(serializers.ModelSerializer) :

	class Meta :
		model = weather
		fields = '__all__'

class historicalSerializer(serializers.ModelSerializer) :

	class Meta :
		model = weather
		fields = ['DATE']
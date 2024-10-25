from rest_framework import serializers
from shop import models

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
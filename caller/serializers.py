from rest_framework import serializers
from .models import UserPhoneLabelMapping


class UserPhoneLabelMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserPhoneLabelMapping
        fields=['username','fullname','phonenumber','label']
        
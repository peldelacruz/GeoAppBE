from rest_framework import serializers
from ..models import CustomUser, Project
from django.contrib.auth.models import User

class ProjectSerializer(serializers.ModelSerializer):
    customusers = serializers.StringRelatedField(many=True)
    class Meta:
        model = CustomUser
        fields =['company','username','customusers']




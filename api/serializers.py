from rest_framework import serializers
from .models import Profile, Operation

# Task1
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # fields = '__all__'
        exclude = ['id']

# Task2
class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ['operation_type', 'x', 'y']

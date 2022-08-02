from rest_framework import serializers
from algorithms.models import *

class AlgorithmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Algorithm
        fields = ('id', 'name', 'description')
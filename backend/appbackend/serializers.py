from rest_framework import serializers
from .models import AB


class ABSerializer(serializers.ModelSerializer):

    class Meta:
        model = AB
        fields = ('a','b','result')
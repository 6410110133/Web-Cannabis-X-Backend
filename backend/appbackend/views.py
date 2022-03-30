from django.shortcuts import render
from .serializers import ABSerializer
from .models import AB
from rest_framework import generics


class ABList(generics.ListCreateAPIView):
    queryset = AB.objects.all()
    serializer_class = ABSerializer
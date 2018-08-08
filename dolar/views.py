from django.shortcuts import render
from rest_framework import viewsets
from .models import Dolar
from .serializers import DolarSerializer

# Create your views here.


class DolarView(viewsets.ModelViewSet):
    queryset = Dolar.objects.all()
    serializer_class = DolarSerializer

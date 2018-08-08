from rest_framework import serializers
from .models import Dolar


class DolarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dolar
        fields = ('id' , 'value' , 'date')

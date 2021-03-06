from django.shortcuts import render
from rest_framework import viewsets
from .models import Dolar
from .serializers import DolarSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
# Create your views here.

@api_view(['GET'])

def usd(request):
    date = request.GET.get('date')
    clp= float(request.GET.get('clp'))
    try:
        dlr = Dolar.objects.get(date=date)
    except Dolar.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        response=clp/float(dlr.value)
        return Response("el valor en dólares "+ str(response)+" del monto en pesos "+str(clp)+", en la fecha "+ str(date))
@api_view(['GET'])

def clp(request):
    date = request.GET.get('date')
    usd = float(request.GET.get('usd'))
    try:
        dlr = Dolar.objects.get(date=date)
    except Dolar.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        response=usd*float(dlr.value)
        return Response("el valor en clp es "+str(response)+" del monto en dolares "+str(usd)+", en la fecha "+ str(date))

@api_view(['GET'])

def dolar_list(request):

    if request.method == 'GET':
        dolars = Dolar.objects.all()
        serializer = DolarSerializer(dolars, many=True)
        return JsonResponse(serializer.data, safe=False)

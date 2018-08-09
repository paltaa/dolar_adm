from django.urls import path, include
from . import  views
from rest_framework import routers

#import scraper


router = routers.DefaultRouter()

router.register('dolar', views.DolarView)

urlpatterns = [
path('', include(router.urls)),
]

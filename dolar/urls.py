from django.urls import path, include
from . import  views
from rest_framework import routers
from django.conf.urls import url


router = routers.DefaultRouter()

#router.register('dolar', views.usd)
#router.register('dolar', views.dolar)

urlpatterns = [
path('', include(router.urls)),
url('usd', views.usd),
url('clp', views.clp),
url('dolar_list', views.dolar_list)
]

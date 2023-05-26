from django.urls import path
from beer.views import *

app_name='alcho'

urlpatterns=[
    path('sai/',sai,name='sai'),
    path('vemula/',vemula,name='vemula'),
]
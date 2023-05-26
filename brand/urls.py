from django.urls import path
from brand.views import *

app_name='kingfis'

urlpatterns=[
    path('shankar/',shankar,name='shankar'),
    path('vemula/',vemula,name='vemula'),
]
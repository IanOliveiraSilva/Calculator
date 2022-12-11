from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', viewHome, name='home'),
    path('addition', viewAddition, name='addition'),
    path('Subtraction', viewSubtraction, name='Subtraction'),
    path('Division', viewDivision, name='Division'),
    path('Multiplication', viewMultiplication, name='Multiplication'),
]
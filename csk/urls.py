from django.urls import path
from csk.views import *

app_name='csk'

urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
    path('raina/',raina,name='raina'),
    path('ruturaj/',ruturaj,name='ruturaj'),
    path('jadeja/',jadeja,name='jadeja'),
    path('rayudu/',rayudu,name='rayudu'),
    path('stokes/',stokes,name='stokes'),
    path('chahar/',chahar,name='chahar'),
    path('dube/',dube,name='dube'),
   
]

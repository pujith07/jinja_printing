from django.urls import path
from rcb.views import *

app_name='rcb'

urlpatterns=[
    path('kholi/',kholi,name='kholi'),
    path('duplessis/',duplessis,name='duplessis'),
    path('abd/',abd,name='abd'),
    path('maxwell/',maxwell,name='maxwell'),
    path('dk/',dk,name='dk'),
    path('hasaranga/',hasaranga,name='hasaranga'),
    path('siraj/',siraj,name='siraj'),
    path('allen/',allen,name='allen'),
    path('sharma/',sharma,name='sharma'),
]
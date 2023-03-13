from django.urls import path
from mi.views import *

app_name='mi'

urlpatterns=[
    path('rohit/',rohit,name='rohit'),
    path('yadav/',yadav,name='yadav'),
    path('pollard/',pollard,name='pollard'),
    path('brevis/',brevis,name='brevis'),
    path('kishan/',kishan,name='kishan'),
    path('david/',david,name='david'),
    path('archer/',archer,name='archer'),
    path('bumrah/',bumrah,name='bumrah'),
    path('sams/',sams,name='sams'),
    path('mills/',mills,name='mills'),
]
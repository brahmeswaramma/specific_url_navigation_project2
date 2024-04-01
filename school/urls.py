from django.urls import path
from school.views import *
app_name='something'
urlpatterns=[
    path('school_list/',school_list,name='school_list'),
]
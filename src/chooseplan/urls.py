from django.urls import path
from django.conf.urls import include, url

from . import views

urlpatterns = [
    path('', views.chooseplan, name='chooseplan'),
    #path('', views.choosesymptoms, name='choosesymptoms'),
]

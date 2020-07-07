from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.selection, name='selection'),
    path('/', views.selection, name='selection'),
    path('<str:room_name>/', views.room, name='room'),
]

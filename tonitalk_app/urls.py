from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room>/', views.get_room, name='get_room'),
    path('check_room', views.check_room, name='home'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.get_messages, name='get_messages'),
]
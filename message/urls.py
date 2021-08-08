from django.urls import path
from . import views


urlpatterns = [
    path('chat/', views.chat, name = 'chat'),
    path('chat/<int:id>/', views.chat_room, name = 'chat_room'),
]
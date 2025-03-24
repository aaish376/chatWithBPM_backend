from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_bpmn, name='upload_bpmn'),
    path('send_query/', views.send_query, name='send_query'),
    path('chats/', views.get_chats, name='get_chats'),
    path('chats/<int:bpmid>/', views.get_chat_messages, name='get_chat_messages'),
    path("chats/<int:bpmid>/delete/", views.delete_chat, name="delete_chat"),
]

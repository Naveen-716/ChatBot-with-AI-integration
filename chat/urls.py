from django.urls import path
from . import views

urlpatterns = [
    path("", views.chat_page, name="chat"),
    path("send/", views.chat_response, name="send"),
]

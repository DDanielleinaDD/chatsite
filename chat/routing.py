# from django.urls import re_path

# from . import consumer

# websocket_urlpatterns = [
#     re_path(r'ws/chat/(?P<room_name>\w+)/$', consumer.ChatConsumer.as_asgi()),
# ]

from django.urls import path
from . import consumer


websocket_urlpatterns = [
    path('<str:user>', consumer.ConnectConsumer.as_asgi()),
    path('chat/<str:room_name>', consumer.ChatConsumer.as_asgi()),
]
from django.urls import re_path
from echo.consumers import EchoConsumers

websocket_urlpatterns = [
    re_path(r'ws/web-socket/$', EchoConsumers.as_asgi()),
]

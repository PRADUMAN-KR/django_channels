from django.urls import path
from . import consumers

websocket_urlpatterns=[
    path('ws/sc/',consumers.MyAsyncConsumer.as_asgi()),
    path('ws/asc/',consumers.MyAsyncConsumer.as_asgi())
]
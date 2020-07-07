# HealthCareNow/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

"""
channel_routing = [
    route('websocket.receive', 'chat.consumers.ws_echo'),
    route('websocket.connect', 'chat.consumers.ws_add',
          path=r'^/chat2/(?P<room>\w+)$'),
]
"""
application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})

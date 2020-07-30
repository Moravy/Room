from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

# it tells Channels what code to run when an HTTP request is received by the Channels server
import chat.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            # routing to chat -> routing -> websocket
            chat.routing.websocket_urlpatterns
        )
    ),
})

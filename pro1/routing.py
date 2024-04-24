# # myproject/routing.py
#
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# import chat.routing
#
# from pro1.chat.consumers import ChatConsumer
#
# form django.urls import path
#
# # when a ws request is given this is how it will be routed
# application = ProtocolTypeRouter({
#
#     #imports authentication
#     'websocket': URLRouter(
#            path('ws/chat/<str:room_name>/',ChatConsumer.as_asgi()),
#         )
#
# })

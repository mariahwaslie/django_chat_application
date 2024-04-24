from django.urls import path

from . import views
app_name = 'chat2'
urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:room_name>/", views.room, name="room"),
    path('/createroom/',views.CreateChatGroup.as_view(),name="createroom"),
    path('joinroom//',views.JoinChatGroup.as_view(),name="join"),
]
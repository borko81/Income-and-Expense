from django.urls import path

from . import views as user_profile_views


app_name = "user_profile"
urlpatterns = [
    path("show_profile/", user_profile_views.show_profile, name="profile"),
    path("delete_profile/<int:id_>/", user_profile_views.delete_profile, name="delete"),
    path("send_message/<int:id_>/", user_profile_views.send_message, name="message_to"),
]

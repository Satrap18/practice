from django.urls import path
from api.views import user_profile, update_user_proflie

urlpatterns = [
    path("user", user_profile, name="user_profile"),
    path("user/<id>/", update_user_proflie, name="update_user_profile"),
]

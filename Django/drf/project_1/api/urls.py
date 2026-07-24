from django.urls import path
from api.views import user_profile

urlpatterns = [
    path("user", user_profile, name="user_profile")
]

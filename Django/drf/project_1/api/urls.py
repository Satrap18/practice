from django.urls import path
from api.views import UserProfileViws

urlpatterns = [
    path("cuser", UserProfileViws.as_view(), name="cuser_profile"),
    path("cuser/<int:id>", UserProfileViws.as_view(), name="cuser_profile_up_de")
]

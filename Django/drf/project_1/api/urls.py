from django.urls import path
from api.views import UserProfileViws, ListUserProfileView, CreateUserProfileView, DeleteUserProfileView, UpdateUserProfileView

urlpatterns = [
    path("cuser", UserProfileViws.as_view(), name="cuser_profile"),
    path("cuser/<int:id>", UserProfileViws.as_view(), name="cuser_profile_up_de"),
    path("guser", ListUserProfileView.as_view(), name="guser_profile"),
    path("guser_create", CreateUserProfileView.as_view(), name="guser_profile_create"),
    path("guser_delete/<int:id>", DeleteUserProfileView.as_view(), name="guser_profile_delete"),
    path("guser_update/<int:id>", UpdateUserProfileView.as_view(), name="guser_profile_update"),
    
]

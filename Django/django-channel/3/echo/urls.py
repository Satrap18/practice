from django.urls import path
from echo.views import EchoViews

urlpatterns = [
    path('', EchoViews.as_view(), name='index')    
]


from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import UserProfile
from api.serializers import UserProfileSerializers
# Create your views here.

@api_view(['get', 'post'])
def user_profile(request):
    
    return Response({"data": "ok"})
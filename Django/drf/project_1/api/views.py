from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.models import UserProfile
from api.serializers import UserProfileSerializers, CreateUserProfileSerializers
# Create your views here.

@api_view(['get', 'post'])
def user_profile(request):
    
    if request.method == "GET":
        data_user = UserProfile.objects.all()
        serializer_data = UserProfileSerializers(data_user, many=True)
        
        return Response(serializer_data.data)
    
    if request.method == "POST":
        
        data_user = request.data
        serializer_data = CreateUserProfileSerializers(data=data_user)
        
        serializer_data.is_valid(raise_exception=True)
        serializer_data.save()
        return Response(serializer_data.data, status=status.HTTP_201_CREATED)
 

@api_view(['put', 'delete'])
def update_user_proflie(request, id):

    if request.method == "PUT":    
        user_profile_obj = UserProfile.objects.get(id=id)
        user_data = request.data
            
        serilizer_data = UserProfileSerializers(
            instance = user_profile_obj,
            data = user_data
        )
            
        serilizer_data.is_valid(raise_exception=True)
            
        serilizer_data.update(
            instance=user_profile_obj,
            validated_data=serilizer_data.validated_data
        )
            
        return Response(serilizer_data.data, status=status.HTTP_200_OK)
    
    if request.method == "DELETE":
        
        user_profile_obj = UserProfile.objects.get(id=id)
        user_profile_obj.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
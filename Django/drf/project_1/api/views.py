from rest_framework.response import Response
from rest_framework import status
from api.models import UserProfile
from api.serializers import UserProfileSerializers, CreateUserProfileSerializers
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class UserProfileViws(APIView):
    
    permission_classes = (IsAuthenticated, )
    
    def get(self, request):
        
        profile_data = UserProfile.objects.all()
        serializers_data = UserProfileSerializers(profile_data, many=True)
        
        return Response(serializers_data.data)
    
    def post(self, request):
        
        user_data = request.data
        serializers_data = CreateUserProfileSerializers(data=user_data)
        serializers_data.is_valid(raise_exception=True)
        serializers_data.save()
        return Response(serializers_data.data, status=status.HTTP_201_CREATED)

    def put(self, request, id):
        
        user_data = request.data
        models_data = UserProfile.objects.get(id=id)
        serializers_data = UserProfileSerializers(instance = models_data, data=user_data)
        serializers_data.is_valid(raise_exception=True)
        serializers_data.update(instance=models_data, validated_data=user_data)
        return Response(serializers_data.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        
        models_data = UserProfile.objects.get(id=id)
        models_data.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
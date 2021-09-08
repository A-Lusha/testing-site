from rest_framework import permissions, status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from users import models, permissions, serializers



# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    """ create and update profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.UpdateOwnProfile, IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'last_name', 'email',)
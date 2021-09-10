from rest_framework import viewsets, filters
from users import models, permissions, serializers



# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    """ create and update profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    permission_classes = [permissions.UpdateOwnProfile]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'last_name', 'email',)
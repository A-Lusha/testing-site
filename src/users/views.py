from django.contrib.auth import get_user_model, models
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from users import permissions, serializers


class UserProfileViewSet(viewsets.ModelViewSet):
    """CRUD for the user profile"""

    serializer_class = serializers.UserProfileSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [permissions.UpdateOwnProfile,]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = (
        'id',
        'first_name',
        'last_name',
        'email',
        'groups',
    )


class GroupAPIView(generics.ListCreateAPIView):
    """CRxx for the Group model"""

    queryset = models.Group.objects.all().order_by("name")
    permission_classes = [permissions.ReadOnly,]
    serializer_class = serializers.GroupSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'name')


class UserLoginAPIView(ObtainAuthToken):
    """Obtain user auth tokens"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
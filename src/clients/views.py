from rest_framework import viewsets, filters
from clients import models, serializers



# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    """ create and update profiles """
    serializer_class = serializers.ClientSerializer
    queryset = models.Client.objects.all()
    # permission_classes = [permissions.UpdateOwnProfile]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'last_name', 'business_name', 'contact_email',)
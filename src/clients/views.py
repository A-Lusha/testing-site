from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ClientSerializer
from .models import Client


# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    """ create and update profiles """
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    # permission_classes = [permissions.UpdateOwnProfile]
    filter_backends = (DjangoFilterBackend,)
    filter_fields = (
            'id',
            'business_name',
            'first_name',
            'last_name',
            'contact_email',
            'assigned_rep__id',
            'status',
            'schedule_sent'
        )


    # search_fields = ('assigned_rep__email',)
    # search_fields = {
    #     'business_name': ['exact', 'istartswith'],
    #     'contact_email': ['exact'],
    #     'assigned_rep__id': ['exact'],
    # }


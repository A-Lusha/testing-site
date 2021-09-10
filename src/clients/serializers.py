from rest_framework import serializers
from clients import models

# https://www.django-rest-framework.org/api-guide/generic-views/#get_serializer_classself
# https://www.django-rest-framework.org/api-guide/serializers/#object-level-validation
# https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation
# will want to implement at least the first one later

class ClientSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.Client
        fields = '__all__'


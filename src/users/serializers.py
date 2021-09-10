from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model, models
from rest_framework import serializers


User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes the UserProfile object"""
    email = serializers.EmailField(max_length=255, validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'groups')
        extra_kwargs = {
            'password': {'write_only': True,
            'style': {'input_type': 'password'}}
        }

    def create(self, validated_data):
        """Create and return a new user where username is also email"""
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        if validated_data['groups']:
            user.groups.set(validated_data['groups'])
        return user


class GroupSerializer(serializers.ModelSerializer):
    """Serializes the Group object"""

    class Meta:
        model = models.Group
        fields = ('id', 'name')
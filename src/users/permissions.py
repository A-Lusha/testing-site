from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Allow users to edit own profile """

    def has_object_permission(self, request, view, obj):
        """Check if editing own profile, readonly - unless is_superuser"""
        if request.user.is_superuser:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


class ReadOnly(permissions.BasePermission):
    """SAFE_METHODS only - pretty self explanatory"""

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

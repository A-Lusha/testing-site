from django.core.exceptions import PermissionDenied


def index(request):
    """Nothing to see here yet, folks"""
    raise PermissionDenied
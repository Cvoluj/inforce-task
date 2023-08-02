from rest_framework.permissions import BasePermission

class CanCreateRestaurant(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated and is_staff is True
        return request.user.is_authenticated and request.user.is_staff
from rest_framework import permissions


class UpdateOwnPermissions(permissions.BasePermission):
    """Update own permissions"""

    def has_object_permission(self, request, view , obj):
        """Check permissions whehter user edit his own permissions """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

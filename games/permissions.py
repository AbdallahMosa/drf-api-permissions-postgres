from rest_framework import permissions

class isOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # allow read-only access to all users
        if request.method == 'GET':
            return True
        if request.user == obj.purchaser:
            return True
        else:
            return False

    
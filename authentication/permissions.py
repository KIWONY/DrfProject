from rest_framework import permissions





# Custom Permission
# if obj.author and reqeust.user are equal, requeset.user doesn't have permission to perform delete and update
class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user

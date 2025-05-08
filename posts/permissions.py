from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Оқу рұқсаты (GET, HEAD, OPTIONS) — барлығына
        if request.method in permissions.SAFE_METHODS:
            return True
        # Тек автор ғана жазып/өшіре алады
        return obj.author == request.user

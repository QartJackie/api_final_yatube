from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Разрешение всех методов для автора."""

    def has_permission(self, request, view):
        """Функция проверки аутентификации пользователя,
        возвращает булевое значение."""
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj) -> bool:
        """Функция проверки авторства, возвращающая булевое значение."""
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )

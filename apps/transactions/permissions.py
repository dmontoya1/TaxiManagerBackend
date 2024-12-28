from rest_framework.permissions import BasePermission


class IsBossOrDriver(BasePermission):
    """
    Permite acceso solo a jefes o taxistas según el contexto.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_boss():
            # El jefe puede ver datos de sus taxistas
            return obj.user.boss == user
        elif user.is_driver():
            # El taxista solo puede ver sus propios datos
            return obj.user == user
        return False

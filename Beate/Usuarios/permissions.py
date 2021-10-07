from rest_framework import permissions
from rest_framework.permissions import BasePermission

class AccesoPersonal(BasePermission):
    def has_object_permission(self, request, view, obj):
        # request => contiene toda la información del usuario
        # obj => corresponde al objeto que se quiere manipular
        
        # Define el acceso si la inforamción que se desea manipular corresponde al mismo usuario
        if request.user.is_staff:
            return True
        return obj.id == request.user.id
        
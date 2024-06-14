# security/permissions.py

from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name == 'admin'

class IsMonitorUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name == 'monitor'

class IsAnalystUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name == 'analyst'
    
class IsAdminOrMonitorOrAnalyst(BasePermission):
    def has_permission(self, request, view):
        # Verifica si el usuario tiene uno de los roles requeridos
        return request.user.is_authenticated and (
            request.user.role.name == 'admin' or request.user.role.name == 'monitor' or request.user.role.name == 'analyst'
        )
    
class IsAdminOrAnalyst(BasePermission):
    def has_permission(self, request, view):
        # Verifica si el usuario tiene uno de los roles requeridos
        return request.user.is_authenticated and (
            request.user.role.name == 'admin' or request.user.role.name == 'analyst'
        )

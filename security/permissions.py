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

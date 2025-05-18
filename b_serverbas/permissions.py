from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.Role >= 1

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)

class WorkerPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.Role == 2 or request.user.Role == 5)

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)

class CompanyPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.Role == 3 or request.user.Role == 5)

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
    
class ManagerPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.Role == 4 or request.user.Role == 5)

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)

class WorkerManagerPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.Role == 2 or request.user.Role == 4 or request.user.Role == 5)

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)

class CompanyManagerPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.Role == 3 or request.user.Role == 4 or request.user.Role == 5)

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)

class WorkerCompanyManagerPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.Role == 2 or request.user.Role == 3
                                                   or request.user.Role == 4 or request.user.Role == 5)

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)

class AdminPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.Role == 5

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)

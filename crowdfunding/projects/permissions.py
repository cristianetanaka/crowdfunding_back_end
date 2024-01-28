from rest_framework import permissions


    
class IsownerOrReadOnly(permissions.BasePermission): # this class represents permissions
    def has_object_permission(self, request, view, obj): # determine whether user has permission for this method
        if request.method in permissions.SAFE_METHODS: # check if user is making get request
            return True
        return obj.owner == request.user
    
class IsPledgeSupporter(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.supporter == request.user
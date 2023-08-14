from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    # def has_permission(self, request, view):
    #     if not request.user.is_staff:
    #         return False
    #
        # return super().has_permission(request, view)

    # def has_permission(self, request, view):
    #     user = request.user
    #     # get_all_permission get all permissions relate to the user
    #     print(user.get_all_permissions())
    #     if user.is_staff:
    #         # cheecking weather this user has these permission if yes return true esle false
    #
    #         if user.has_perm("products.view_product"):  # !appname.verb_model_name
    #             return True
    #         if user.has_perm("products.add_product"):
    #             return True
    #         if user.has_perm("products.change_product"):
    #             return True
    #         if user.has_perm("products.delete_product"):
    #             return True
    #         # keeping the defaults
    #         return False
    #     print(user.get_all_permissions())
    #     return False

# --------------------------note-------------------------------------------
# def has_object_permission(self, request, view, obj):
#         or Check weather it is in the safe methods  --> like
#    """
#     Object-level permission to only allow owners of an object to edit it.
#     Assumes the model instance has an `owner` attribute.
#     """
#
#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request,
#         # so we'll always allow GET, HEAD or OPTIONS requests.
#         if request.method in permissions.SAFE_METHODS:
#             return True
#
#         # Instance must have an attribute named `owner`.
#         return obj.owner == request.user

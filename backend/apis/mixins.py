from .permissions import IsStaffEditorPermission
from rest_framework import permissions
from products.models  import Product
class StaffEditorPermissionMixin():
    permission_classes = [
        permissions.IsAdminUser,
        IsStaffEditorPermission
    ]

class UserQuerySetMixin():
    user_field = 'user'
    # allow_staff_view = False
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        request = self.request
        user = request.user
        print(user)
        lookup_data = {}
        lookup_data[self.user_field] = user
        if user.is_staff:
            return qs
        return qs.filter(**lookup_data)


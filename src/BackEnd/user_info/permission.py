from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.authentication  import JWTAuthentication

from user_info.models import UserType
from utils.api import get_user_and_token_by_jwt_request


class IsAdminUserPermission(BasePermission):

    def has_permission(self, request, view):
        user, token = get_user_and_token_by_jwt_request(request)
        return (user.user_type == UserType.ADMIN_USER)
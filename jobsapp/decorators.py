from functools import wraps
from django.core.exceptions import PermissionDenied


def role_required(role):
    def decorator(function):
        @wraps(function)
        def wrap(request, *args, **kwargs):
            if not request.user.is_authenticated or request.user.role != role:
                raise PermissionDenied
            return function(request, *args, **kwargs)
        return wrap
    return decorator


def user_is_employer(function):
    return role_required('employer')(function)


def user_is_employee(function):
    return role_required('employee')(function)

from functools import wraps
from http import HTTPStatus
from types import SimpleNamespace

from flask import request, g

from api.security.auth0_service import auth0_service
from api.utils import json_abort

unauthorized_error = {
    "message": "Requires authentication"
}

invalid_request_error = {
    "error": "invalid_request",
    "error_description": "Authorization header value must follow this format: Bearer access-token",
    "message": "Requires authentication"
}

admin_messages_permissions = SimpleNamespace(
    read="read:admin-messages"
)


def get_bearer_token_from_request():
    authorization_header = request.headers.get("Authorization", None)

    if not authorization_header:
        json_abort(HTTPStatus.UNAUTHORIZED, unauthorized_error)
        return

    authorization_header_elements = authorization_header.split()

    if len(authorization_header_elements) != 2:
        json_abort(HTTPStatus.BAD_REQUEST, invalid_request_error)
        return

    auth_scheme = authorization_header_elements[0]
    bearer_token = authorization_header_elements[1]

    if not (auth_scheme and auth_scheme.lower() == "bearer"):
        json_abort(HTTPStatus.UNAUTHORIZED, unauthorized_error)
        return

    if not bearer_token:
        json_abort(HTTPStatus.UNAUTHORIZED, unauthorized_error)
        return

    return bearer_token


def authorization_guard(function):
    @wraps(function)
    def decorator(*args, **kwargs):
        token = get_bearer_token_from_request()
        validated_token = auth0_service.validate_jwt(token)

        g.access_token = validated_token

        return function(*args, **kwargs)

    return decorator


def permissions_guard(required_permissions=None):
    def decorator(function):
        @wraps(function)
        def wrapper():
            access_token = g.get("access_token")

            if not access_token:
                json_abort(401, unauthorized_error)
                return

            if required_permissions is None:
                return function()

            if not isinstance(required_permissions, list):
                json_abort(500, {
                    "message": "Internal Server Error"
                })

            token_permissions = access_token.get("permissions")

            if not token_permissions:
                json_abort(403, {
                    "message": "Permission denied"
                })

            required_permissions_set = set(required_permissions)
            token_permissions_set = set(token_permissions)

            if not required_permissions_set.issubset(token_permissions_set):
                json_abort(403, {
                    "message": "Permission denied"
                })

            return function()

        return wrapper

    return decorator

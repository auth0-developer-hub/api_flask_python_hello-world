from functools import wraps
from http import HTTPStatus

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

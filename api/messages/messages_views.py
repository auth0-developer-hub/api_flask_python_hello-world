from flask import (
    Blueprint
)

from api.messages.messages_service import (
    get_public_message,
    get_protected_message,
    get_admin_message
)
from api.security.guards import (
    authorization_guard,
    permissions_guard,
    admin_messages_permissions
)

bp_name = 'api-messages'
bp_url_prefix = '/api/messages'
bp = Blueprint(bp_name, __name__, url_prefix=bp_url_prefix)


@bp.route("/public")
def public():
    return {
        "text": get_public_message().text
    }


@bp.route("/protected")
@authorization_guard
def protected():
    return {
        "text": get_protected_message().text
    }


@bp.route("/admin")
@authorization_guard
@permissions_guard([admin_messages_permissions.read])
def admin():
    return {
        "text": get_admin_message().text
    }

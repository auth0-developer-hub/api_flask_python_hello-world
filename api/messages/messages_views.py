from flask import (
    Blueprint
)

from api.messages.messages_service import (
    get_public_message,
    get_protected_message,
    get_admin_message
)

bp_name = 'api-messages'
bp_url_prefix = '/api/messages'
bp = Blueprint(bp_name, __name__, url_prefix=bp_url_prefix)


@bp.route("/public")
def public():
    return get_public_message().__dict__


@bp.route("/protected")
def protected():
    return get_protected_message().__dict__


@bp.route("/admin")
def admin():
    return get_admin_message().__dict__

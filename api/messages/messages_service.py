from api.messages.message import Message


def get_public_message():
    return Message(
        "The API doesn't require an access token to share this message."
    )


def get_protected_message():
    return Message(
        "The API successfully validated your access token."
    )


def get_admin_message():
    return Message(
        "The API successfully recognized you as an admin."
    )

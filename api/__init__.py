##########################################
# External Modules
##########################################

import os

from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

from api import exception_views
from api.messages import messages_views


def create_app():
    ##########################################
    # Environment Variables
    ##########################################
    client_origin_url = os.environ.get("CLIENT_ORIGIN_URL")

    if not client_origin_url:
        raise NameError("The required environment variables are missing. Check .env file.")

    ##########################################
    # Flask App Instance
    ##########################################

    app = Flask(__name__, instance_relative_config=True)

    ##########################################
    # HTTP Security Headers
    ##########################################

    csp = {
        'default-src': ['\'self\''],
        'frame-ancestors': ['\'none\'']
    }

    Talisman(app,
             frame_options='DENY',
             content_security_policy=csp,
             referrer_policy='no-referrer'
             )

    @app.after_request
    def add_headers(response):
        response.headers['X-XSS-Protection'] = '0'
        response.headers['Cache-Control'] = 'no-store, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        return response

    ##########################################
    # CORS
    ##########################################

    CORS(
        app,
        resources={r"/api/*": {"origins": client_origin_url}},
        allow_headers=["Authorization", "Content-Type"],
        methods=["GET"],
        max_age=86400
    )

    ##########################################
    # Blueprint Registration
    ##########################################

    app.register_blueprint(messages_views.bp)
    app.register_blueprint(exception_views.bp)

    return app

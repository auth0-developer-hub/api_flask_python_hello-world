import gunicorn.http.wsgi
from functools import wraps
from dotenv import load_dotenv
from common.utils import safe_get_env_var

load_dotenv()

wsgi_app = "api.wsgi:app"
bind = f"0.0.0.0:{safe_get_env_var('PORT')}"

def wrap_default_headers(func):
    @wraps(func)
    def default_headers(*args, **kwargs):
        return [header for header in func(*args, **kwargs) if not header.startswith('Server: ')]
    return default_headers

gunicorn.http.wsgi.Response.default_headers = wrap_default_headers(gunicorn.http.wsgi.Response.default_headers)

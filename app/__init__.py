from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from .endpoints import endpoints_bp
from .config import get_config


def create_app(env_name='default'):
    cfg = get_config(env_name)
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.url_map.strict_slashes = False
    app.config.from_object(cfg)
    register_buleprint(app)
    return app


def register_buleprint(app):
    app.register_blueprint(endpoints_bp, url_prefix="/")

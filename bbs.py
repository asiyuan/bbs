from flask import Flask
from app.cms import bp as cms_bp
from app.common import bp as common_bp
from app.front import bp as front_bp
from app.ueditor import bp as ueditor_bp
import config
from exts import db,mail
from flask_wtf import CSRFProtect

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(cms_bp)
    app.register_blueprint(common_bp)
    app.register_blueprint(front_bp)
    app.register_blueprint(ueditor_bp)

    db.init_app(app)
    mail.init_app(app)
    CSRFProtect(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=2000)

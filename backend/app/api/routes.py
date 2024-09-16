from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.app.api.auth import auth_bp
from backend.app.api.applications import applications_bp
from backend.app.api.webhooks import webhooks_bp

api_bp = Blueprint('api', __name__)

def register_routes(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(applications_bp, url_prefix='/applications')
    app.register_blueprint(webhooks_bp, url_prefix='/webhooks')
    app.register_blueprint(api_bp, url_prefix='/api')
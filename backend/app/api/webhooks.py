from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.app.db.models import Webhook
from backend.app.services.webhook_service import register_webhook, update_webhook, delete_webhook

webhooks_bp = Blueprint('webhooks', __name__)

@webhooks_bp.route('/', methods=['GET'])
@jwt_required()
def get_webhooks():
    user_id = get_jwt_identity()
    webhooks = Webhook.query.filter_by(user_id=user_id).all()
    webhooks_data = [webhook.to_dict() for webhook in webhooks]
    return jsonify(webhooks=webhooks_data), 200

@webhooks_bp.route('/', methods=['POST'])
@jwt_required()
def register_new_webhook():
    user_id = get_jwt_identity()
    webhook_data = request.json

    # HUMAN ASSISTANCE NEEDED
    # Implement proper validation for webhook_data
    if not webhook_data or 'url' not in webhook_data:
        return jsonify(error="Invalid webhook data"), 400

    new_webhook = register_webhook(user_id, webhook_data)
    db.session.add(new_webhook)
    db.session.commit()

    return jsonify(webhook=new_webhook.to_dict()), 201

@webhooks_bp.route('/<webhook_id>', methods=['PUT'])
@jwt_required()
def update_existing_webhook(webhook_id):
    user_id = get_jwt_identity()
    webhook = Webhook.query.filter_by(id=webhook_id, user_id=user_id).first()

    if not webhook:
        return jsonify(error="Webhook not found"), 404

    updated_data = request.json

    # HUMAN ASSISTANCE NEEDED
    # Implement proper validation for updated_data
    if not updated_data:
        return jsonify(error="Invalid webhook data"), 400

    updated_webhook = update_webhook(webhook, updated_data)
    db.session.commit()

    return jsonify(webhook=updated_webhook.to_dict()), 200

@webhooks_bp.route('/<webhook_id>', methods=['DELETE'])
@jwt_required()
def delete_existing_webhook(webhook_id):
    user_id = get_jwt_identity()
    webhook = Webhook.query.filter_by(id=webhook_id, user_id=user_id).first()

    if not webhook:
        return jsonify(error="Webhook not found"), 404

    delete_webhook(webhook)
    db.session.delete(webhook)
    db.session.commit()

    return jsonify(message="Webhook deleted successfully"), 200
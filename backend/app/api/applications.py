from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.app.db.models import Application
from backend.app.services.document_classifier import classify_document
from backend.app.services.ocr_service import extract_application_data

applications_bp = Blueprint('applications', __name__)

@applications_bp.route('/', methods=['GET'])
@jwt_required()
def get_applications():
    user_id = get_jwt_identity()
    applications = Application.query.filter_by(user_id=user_id).all()
    applications_data = [app.to_dict() for app in applications]
    return jsonify(applications=applications_data), 200

@applications_bp.route('/<application_id>', methods=['GET'])
@jwt_required()
def get_application(application_id):
    user_id = get_jwt_identity()
    application = Application.query.filter_by(id=application_id, user_id=user_id).first_or_404()
    return jsonify(application=application.to_dict()), 200

@applications_bp.route('/', methods=['POST'])
@jwt_required()
def create_application():
    # HUMAN ASSISTANCE NEEDED
    # This function needs additional error handling and data validation
    user_id = get_jwt_identity()
    data = request.get_json()
    
    # Validate application data
    if not data or 'application_type' not in data:
        return jsonify(error="Invalid application data"), 400
    
    new_application = Application(
        user_id=user_id,
        application_type=data['application_type'],
        status='pending',
        # Add other fields as necessary
    )
    
    # Save application to database
    db.session.add(new_application)
    db.session.commit()
    
    return jsonify(application=new_application.to_dict()), 201

@applications_bp.route('/<application_id>', methods=['PUT'])
@jwt_required()
def update_application(application_id):
    # HUMAN ASSISTANCE NEEDED
    # This function needs additional error handling and data validation
    user_id = get_jwt_identity()
    application = Application.query.filter_by(id=application_id, user_id=user_id).first_or_404()
    
    data = request.get_json()
    
    # Validate updated application data
    if not data:
        return jsonify(error="Invalid application data"), 400
    
    # Update fields
    for key, value in data.items():
        if hasattr(application, key):
            setattr(application, key, value)
    
    # Save updated application to database
    db.session.commit()
    
    return jsonify(application=application.to_dict()), 200
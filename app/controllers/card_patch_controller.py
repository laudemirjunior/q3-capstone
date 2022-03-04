from http import HTTPStatus

from flask import current_app, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.models.card_model import CardModel

@jwt_required()
def update_card():
    pass
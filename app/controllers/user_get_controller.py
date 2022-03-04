from http import HTTPStatus

from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.models.user_model import UserModel


@jwt_required()
def user_get():
    user_query = UserModel.query
    email = get_jwt_identity().get('email')
    user: UserModel = user_query.filter_by(email=email).first()    

    return jsonify(user.activities), HTTPStatus.OK

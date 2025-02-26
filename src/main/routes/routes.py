#pylint:disable=W0718,W0611
from flask import Blueprint, request, jsonify

# Import adatpters
from src.main.adapters.request_adapter import request_adapter

# Import composers
from src.main.composers.authenticate_token_composer import authenticate_token_composer
from src.main.composers.change_username_composer import change_username_composer
from src.main.composers.create_user_composer import create_user_composer
from src.main.composers.delete_user_composer import delete_user_composer
from src.main.composers.login_case_composer import login_case_composer
from src.main.composers.select_composer import select_user_composer

# Import Validators
from src.validators.request_validators.create_user_validator_request import create_user_validator

# Import error handler
from src.errors.error_handler import error_handler

# Import Authentication
from src.main.middlewares.auth_middleware import require_authentication

user_routes_bp = Blueprint("user_routes", __name__)

@user_routes_bp.route("/user/register", methods=["POST"])
def register_user() -> any:
    http_response = None

    try:
        create_user_validator(request)
        http_response = request_adapter(request, create_user_composer())
    except Exception as e:
        http_response = error_handler(e)
    
    return jsonify(http_response.body), http_response.status_code

@user_routes_bp.route("/user/login", methods=["POST"])
def login_user() -> any:
    http_response = None

    try:
        http_response = request_adapter(request, login_case_composer())
    except Exception as e:
        http_response = error_handler(e)
    
    return jsonify(http_response.body), http_response.status_code
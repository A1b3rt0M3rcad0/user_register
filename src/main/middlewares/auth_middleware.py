from flask import request, jsonify
from functools import wraps
from src.main.composers.authenticate_token_composer import authenticate_token_composer
from src.main.adapters.request_adapter import request_adapter

def require_authentication(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"error": "Token not found"}), 401
        
        auth_result = request_adapter(request, authenticate_token_composer())

        if auth_result.status_code != 200:
            return jsonify(auth_result.body), auth_result.status_code
        
        return f(token=token, *args, **kwargs)
    
    return decorated_function
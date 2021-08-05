from flask      import jsonify, request
from jsonschema import validate, ValidationError
from functools  import wraps

from config     import SIGNUP_SCHEMA

# 회원가입 유효성 검사 
def signup_validator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            validate(request.get_json(), SIGNUP_SCHEMA)
        
        except ValidationError as e:
            return jsonify({"message" : e.message}), 422
        
        return func(*args, **kwargs)
    return wrapper
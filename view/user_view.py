from flask       import request, jsonify
from flask.views import MethodView
from jsonschema  import validate, ValidationError

from connection              import connect_db
from service.user_service    import UserService
from config                  import SIGNUP_SCHEMA

class UserView(MethodView):
    def post(self):
        # 회원가입(사용자 생성)
        user_service = UserService()
        connection   = None
        user_info    = request.get_json() 
            
        try:
            validate(user_info, SIGNUP_SCHEMA)

            connection = connect_db()
            result = user_service.signup(user_info, connection)
            connection.commit()

            return jsonify({"message" : "Account is created successfully.",
                            "data"    : result}), 201
        
        except ValidationError as e:
            raise e
        
        except Exception as e:
            connection.rollback()
            raise e
        
        finally:
            if connection is not None:
                connection.close()
    
    def get(self):
        # 회원정보 조회 (단일, 전체)
        pass
    
    def delete(self):
        # 회원정보 삭제
        pass
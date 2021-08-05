from flask       import request, jsonify
from flask.views import MethodView

from connection              import connect_db
from service.user_service    import UserService
from utils                   import signup_validator

class UserView(MethodView):
    @signup_validator
    def post(self):
        # 회원가입(사용자 생성)
        user_service = UserService()
        connection   = None
            
        try:
            user_info    = request.get_json() 

            connection = connect_db()
            result = user_service.signup(user_info, connection)
            connection.commit()

            return jsonify({"message" : "Account is created successfully.",
                            "data"    : result}), 201
        
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
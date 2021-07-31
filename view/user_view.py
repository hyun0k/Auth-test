from flask       import request, jsonify
from flask.views import MethodView

from connection              import connect_db
from service.user_service    import UserService

class UserView(MethodView):
    def post(self):
        # 회원가입(사용자 생성)
        user_service = UserService()
        connection = None
        try:
            user_info = request.get_json() # TODO - 파라미터 유효성 검사 필요. 데코레이터로 jsonschema 사용 예정.
            
            connection = connect_db()
            result = user_service.signup(user_info, connection)
            connection.commit()

            return jsonify({"message" : "Account is created successfully.",
                            "data"    : result}), 201
        
        except Exception as e:
            connection.rollback()
            raise e
        
    
    def get(self):
        # 회원정보 조회 (단일, 전체)
        pass
    
    def delete(self):
        # 회원정보 삭제
        pass
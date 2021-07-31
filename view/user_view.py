from flask       import jsonify
from flask.views import MethodView

from connection import connect_db

class UserView(MethodView):
    def post(self):
        # 회원가입(사용자 생성)
        pass
    
    def get(self):
        # 회원정보 조회 (단일, 전체)
        pass
    
    def delete(self):
        # 회원정보 삭제
        pass
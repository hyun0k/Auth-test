import bcrypt
import hashlib
import jwt

from model.user_dao import UserDao

class UserService:
    def signup(self, data, connection):
        user_dao = UserDao()

        hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8') # TODO 암호화 방법 스터디 후 bcrypt와 hashlib 조합하여 활용하는 방식으로 바꿀 것.
        data['password'] = hashed_password

        return user_dao.signup(data, connection)

        
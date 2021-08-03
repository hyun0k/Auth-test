import bcrypt
import hashlib
import base64
import jwt

from model.user_dao import UserDao

class UserService:
    def signup(self, data, connection):
        user_dao = UserDao()
        
        hashed_password = str(bcrypt.hashpw(base64.b64encode(hashlib.sha256(bytes(data['password'], 'utf-8')).digest()), bcrypt.gensalt()), 'utf-8')
        data['password'] = hashed_password
        
        return user_dao.signup(data, connection)

        
import pymysql

class UserDao:
    def signup(self, data, connection):
        query = """
            INSERT INTO users(
                user_id,
                password,
                name,
                email,
                phone_number,
                created_at,
                is_deleted
            )
            VALUES(
                %(user_id)s,
                %(password)s,
                %(name)s,
                %(email)s,
                %(phone_number)s,
                NOW(),
                0
            )
        """

        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query, data)
            return cursor.lastrowid
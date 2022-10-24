from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.f_name = data['first_name']
        self.l_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES(%(fn)s, %(ln)s, %(email)s);"
        connectToMySQL('users').query_db(query,data)
        return

    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name = %(fn)s, last_name = %(ln)s, email = %(email)s WHERE id = %(id)s;"
        connectToMySQL('users').query_db(query,data)
        return

    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        connectToMySQL('users').query_db(query,data)
        return
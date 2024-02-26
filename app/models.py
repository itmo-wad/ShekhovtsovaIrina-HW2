from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from app import mongo

class UserProfile(UserMixin):
    def __init__(self, login, password):
        self.login = login
        self.password_hash = password

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def save_to_db(self):
        user_data = {
            'login': self.login,
            'password_hash': self.password_hash
        }
        mongo.db.personal.insert_one(user_data)

    def get_id(self):
        return self.login


@login.user_loader
def load_user(username):
    u = mongo.db.personal.find_one({"login": username})
    if not u:
        return None
    return UserProfile(login=u['login'],password=u['password_hash'])


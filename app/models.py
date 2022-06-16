import sqlalchemy as sa
from app import db, app
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from users_policy import UsersPolicy


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(256), nullable=False)

    last_name = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100))

    created_at = db.Column(db.DateTime, nullable=False, server_default=sa.sql.func.now())
    role = db.Column(db.Integer,  db.ForeignKey('roles.id'), nullable=False)

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str):
        return check_password_hash(self.password_hash, password)

    @property
    def full_name(self):
        return ' '.join([self.last_name, self.first_name, self.middle_name or ''])

    @property
    def is_admin(self):
        return app.config.get('ADMIN_ROLE_ID') == self.role_id

    @property
    def is_moder(self):
        return app.config.get('MODER_ROLE_ID') == self.role_id

    def can(self, action, record = None):
        user_policy = UsersPolicy(record=record)
        method = getattr(user_policy, action, None)
        if method is not None: return method()
        else: return False

    def __repr__(self):
        return '<User %r>' % self.login

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    desc = db.Column(db.Text)

    def __repr__(self):
        return '<Role %r>' % self.name
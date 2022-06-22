import os
from flask import url_for
import sqlalchemy as sa
from app import db, app
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from users_policy import UsersPolicy
from sqlalchemy.dialects.mysql import YEAR
from markdown import markdown


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(256), nullable=False)

    last_name = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100))

    created_at = db.Column(db.DateTime, nullable=False, server_default=sa.sql.func.now())
    role_id = db.Column(db.Integer,  db.ForeignKey('roles.id'), nullable=False)

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
    desc = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Role %r>' % self.name

class Image(db.Model):
    _tablename__ = 'images'

    id = db.Column(db.String(100), primary_key=True)
    file_name = db.Column(db.String(100), nullable=False)
    mime_type = db.Column(db.String(100), nullable=False)
    md5_hash = db.Column(db.String(100), nullable=False, unique=True)
    
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)

    def __repr__(self):
        return '<Image %r>' % self.file_name

    @property
    def storage_filename(self):
        _, ext = os.path.splitext(self.file_name)
        return self.id + ext

    @property
    def url(self):
        return url_for('image', image_id=self.id)

books_genres = db.Table('books_genres',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), nullable=False),
    db.Column('genre_id', db.Integer, db.ForeignKey('genres.id'), nullable=False)
)


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    desc = db.Column(db.Text, nullable=False)
    year = db.Column(YEAR, nullable=False)
    publisher = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    volume = db.Column(db.Integer, nullable=False)
    rating_sum = db.Column(db.Integer, nullable=False, default=0)
    rating_num = db.Column(db.Integer, nullable=False, default=0)

    genres = db.relationship('Genre', secondary=books_genres, lazy='subquery')
    reviews = db.relationship('Review', cascade="all, delete")
    image = db.relationship('Image', cascade="all, delete", uselist=False)

    def update(self, params, genres_ids):
        self.name = params['name']
        self.desc = params['desc']
        self.year = params['year']
        self.publisher = params['publisher']
        self.author = params['author']
        self.volume = params['volume']

        for id in genres_ids:
            genre = Genre.query.get(id)
            self.genres.append(genre)

    @property
    def rating(self):
        if self.rating_num > 0:
            return self.rating_sum / self.rating_num
        else:
            return 0

    @property
    def html_desc(self):
        return markdown(self.desc)

    def __repr__(self):
        return '<Book %r>' % self.name


class Review(db.Model):
    __tablename__='reviews'

    id = db.Column(db.Integer, primary_key=True)

    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=sa.sql.func.now())
    status_id = db.Column(db.Integer, db.ForeignKey('statuses.id'), nullable=False, default=0)

    user = db.relationship('User', uselist=False)
    book = db.relationship('Book', uselist=False)

    @property
    def html_text(self):
        return markdown(self.text)

class Genre(db.Model):
    __tablename__='genres'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)

class Status(db.Model):
    __tablename__='statuses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
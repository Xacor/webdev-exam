import os
from flask import Flask, abort, render_template, send_file, session, request, redirect, url_for, flash
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)

from auth import bp as auth_bp, init_login_manager
from books import bp as books_bp
from reviews import bp as reviews_bp

app.register_blueprint(auth_bp)
app.register_blueprint(books_bp)
app.register_blueprint((reviews_bp))
init_login_manager(app)



PER_PAGE = 4
from models import Book, Image
@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)

    books = Book.query.order_by(Book.year.desc())
    pagination = books.paginate(page, PER_PAGE)
    books = pagination.items


    return render_template('index.html', 
                            books=books, 
                            pagination=pagination,
                            )

@app.route('/media/images/<image_id>')
def image(image_id):
    image = Image.query.get(image_id)
    if image:
        return send_file(os.path.join(app.config['UPLOAD_FOLDER'], image.storage_filename))
    return abort(404)
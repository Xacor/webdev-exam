from flask import Blueprint, redirect, render_template, request, flash, url_for
from models import Book, Genre
from app import db

bp = Blueprint('books', __name__, url_prefix='/books')

PER_PAGE = 4

BOOK_PARAMS = ['name','desc' ,'year', 'publisher', 'author', 'volume']

def params(param):
    return {p: request.form.get(p) for p in param }



@bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)

    books = Book.query.all()
    pagination = books.paginate(page, PER_PAGE)
    books = pagination.items


    return render_template('books/index.html', 
                            books=books, 
                            pagination=pagination,
                            )

@bp.route('/new')
def new():
    genres = Genre.query.all()
    return render_template('books/new.html', genres=genres)

@bp.route('/create', methods=['POST'])
def create():
    book = Book(**params(BOOK_PARAMS))

    genres_ids = list(map(int, request.form.getlist('genres')))
    for id in genres_ids:
        genre = Genre.query.get(id)
        book.genres.append(genre)

    db.session.add(book)
    db.session.commit()

    # print(params(BOOK_PARAMS), genres_ids)
    return redirect(url_for('index')) #переделать редирект

@bp.route('/update')
def update():
    genres = Genre.query.all()
    return render_template('books/update.html', genres=genres)

@bp.route('/show/<int:book_id>')
def show(book_id):
    book = Book.query.get(book_id)
    return render_template('books/show.html', book=book)
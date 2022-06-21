from flask import Blueprint, redirect, render_template, request, flash, url_for
from flask_login import current_user, login_required
from auth import check_rights
from models import Book, Genre, Review
from app import db
from markdown import markdown
from bleach import clean
from sqlalchemy.exc import SQLAlchemyError
from tools import ImageSaver

bp = Blueprint('books', __name__, url_prefix='/books')

PER_PAGE = 4

BOOK_PARAMS = ['name','desc' ,'year', 'publisher', 'author', 'volume']
REVIEW_PARAMS = ['rating', 'text']

def params(param):
    return {p: clean(request.form.get(p)) for p in param }



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
@login_required
@check_rights('create_book')
def new():
    genres = Genre.query.all()
    return render_template('books/new.html', genres=genres)

@bp.route('/create', methods=['POST'])
@login_required
@check_rights('create_book')
def create():
    book = Book(**params(BOOK_PARAMS))

    genres_ids = list(map(int, request.form.getlist('genres')))
    for id in genres_ids:
        genre = Genre.query.get(id)
        book.genres.append(genre)

    

    try:
        db.session.add(book)
        db.session.commit()
    except SQLAlchemyError as e: 
        db.session.rollback()
        flash(f'При добавлении данных произошла ошибка. \n{e}', category='danger')
        return redirect(url_for('index'))
    f = request.files.get('preview_img')
    if f and f.filename:
        img = ImageSaver(f).save(book.id)
        if not img:
            return redirect(url_for('index'))

        book.image.append(img)
        db.session.add(book)
        db.session.commit()

    flash('Книга успешно создана.',category='success')
    return redirect(url_for('books.show', book_id=book.id))

@bp.route('/<int:book_id>/edit')
@login_required
def edit(book_id):
    genres = Genre.query.all()
    book = Book.query.get(book_id)

    return render_template('books/edit.html', genres=genres, book=book)

@bp.route('/<int:book_id>/update', methods=['POST'])
@login_required
@check_rights('update_book')
def update(book_id):
    book = Book.query.get(book_id)
    genres_ids = list(map(int, request.form.getlist('genres')))
    book.update(params(BOOK_PARAMS), genres_ids)

    db.session.add(book)
    db.session.commit()

    return redirect(url_for('books.show', book_id=book_id))

@bp.route('/<int:book_id>')
def show(book_id):
    book = Book.query.get(book_id)
    desc = markdown(book.desc)

    reviews = Review.query.filter(Review.book_id == book_id).order_by(Review.created_at.desc())

    curr_review = None
    if current_user.is_authenticated:
        curr_review = Review.query.filter(Review.book_id == book_id).filter(Review.user_id == current_user.id).first()
    return render_template('books/show.html', book=book, desc=desc, curr_review=curr_review, reviews=reviews)


@bp.route('/<int:book_id>/review')
@login_required
def review(book_id):
    return render_template('books/review.html', book_id=book_id)


@bp.route('/<int:book_id>/review/create', methods=['POST'])
@login_required
@check_rights('create_review')
def create_review(book_id):
    new_review = Review(**params(REVIEW_PARAMS), book_id=book_id, user_id=current_user.id)
    db.session.add(new_review)

    book = Book.query.get(book_id)
    book.rating_num += 1
    book.rating_sum += int(new_review.rating)

    db.session.commit()
    return redirect(url_for('books.show', book_id=book.id))

@bp.route('/<int:book_id>/delete',  methods=['POST'])
@login_required
@check_rights('delete_book')
def delete(book_id):
    book = Book.query.get(book_id)
    
    try:
        db.session.delete(book)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(f'При удалении данных возникла ошибка. \n{e}', category='danger')
        return redirect(url_for('index'))

    flash('Книга успешно удалена',category='success')
    return redirect(url_for('index'))

#sqlalchemy.exc.IntegrityError
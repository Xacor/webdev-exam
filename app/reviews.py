from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from auth import check_rights
from models import Review
from app import db
from sqlalchemy.exc import SQLAlchemyError

bp = Blueprint('reviews', __name__, url_prefix='/reviews')
PER_PAGE = 10


@bp.route('user_reviews')
@login_required
def user_reviews():
    reviews = Review.query.filter_by(user_id=current_user.id).all()
    return render_template('reviews/user_reviews.html', reviews=reviews)

@bp.route('moderate_reviews')
@login_required
@check_rights('update_review')
def moderate_reviews():
    reviews = Review.query.filter(Review.status_id == 1).order_by(Review.created_at.desc())
    
    page = request.args.get('page', 1, type=int)
    pagination = reviews.paginate(page, PER_PAGE)
    reviews = pagination.items
    return render_template('reviews/moderate_reviews.html', reviews=reviews, pagination=pagination)

@bp.route('/<int:review_id>')
def read(review_id):
    review = Review.query.get(review_id)
    return render_template('reviews/review.html', review=review)

@bp.route('/<int:review_id>/update')
@login_required
@check_rights('update_review')
def update(review_id):
    review = Review.query.get(review_id)
    accept = request.args.get('accept')
    if accept:
        review.status_id = 2
    else:
        review.status_id = 3
    
    try:
        db.session.add(review)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(f'При изменении статуса возникла ошибка. \n{e}', category='danger')
        return redirect(url_for('reviews.read', review_id=review_id))

    flash('Статус успешно изменен.', category='success')
    return redirect(url_for('reviews.moderate_reviews'))
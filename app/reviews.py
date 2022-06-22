from flask import Blueprint, render_template
from flask_login import current_user
from models import Review

bp = Blueprint('reviews', __name__, url_prefix='/reviews')

@bp.route('user_reviews')
def user_reviews():
    reviews = Review.query.filter_by(user_id=current_user.id).all()
    return render_template('reviews/user_reviews.html', reviews=reviews)
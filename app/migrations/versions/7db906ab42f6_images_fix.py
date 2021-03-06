"""Images fix

Revision ID: 7db906ab42f6
Revises: 
Create Date: 2022-06-21 18:27:17.513567

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7db906ab42f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('desc', sa.Text(), nullable=False),
    sa.Column('year', mysql.YEAR(), nullable=False),
    sa.Column('publisher', sa.String(length=200), nullable=False),
    sa.Column('author', sa.String(length=200), nullable=False),
    sa.Column('volume', sa.Integer(), nullable=False),
    sa.Column('rating_sum', sa.Integer(), nullable=False),
    sa.Column('rating_num', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_books')),
    sa.UniqueConstraint('name', name=op.f('uq_books_name'))
    )
    op.create_table('genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_genres')),
    sa.UniqueConstraint('name', name=op.f('uq_genres_name'))
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('desc', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_roles')),
    sa.UniqueConstraint('name', name=op.f('uq_roles_name'))
    )
    op.create_table('books_genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name=op.f('fk_books_genres_book_id_books')),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], name=op.f('fk_books_genres_genre_id_genres')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_books_genres'))
    )
    op.create_table('image',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('file_name', sa.String(length=100), nullable=False),
    sa.Column('mime_type', sa.String(length=100), nullable=False),
    sa.Column('md5_hash', sa.String(length=100), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name=op.f('fk_image_book_id_books')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_image')),
    sa.UniqueConstraint('md5_hash', name=op.f('uq_image_md5_hash'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=100), nullable=False),
    sa.Column('password_hash', sa.String(length=256), nullable=False),
    sa.Column('last_name', sa.String(length=100), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=False),
    sa.Column('middle_name', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], name=op.f('fk_users_role_id_roles')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('login', name=op.f('uq_users_login'))
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name=op.f('fk_reviews_book_id_books')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_reviews_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_reviews'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    op.drop_table('users')
    op.drop_table('image')
    op.drop_table('books_genres')
    op.drop_table('roles')
    op.drop_table('genres')
    op.drop_table('books')
    # ### end Alembic commands ###

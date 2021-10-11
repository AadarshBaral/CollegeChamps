"""empty message

Revision ID: c22837f5c477
Revises: 
Create Date: 2021-10-11 12:52:52.558246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c22837f5c477'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('slug', sa.String(length=100), nullable=False),
    sa.Column('subtitle', sa.Text(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('img', sa.Text(), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('image_file', sa.String(length=20), nullable=True),
    sa.Column('mock_title', sa.String(length=20), nullable=True),
    sa.Column('mock_content', sa.String(length=200), nullable=True),
    sa.Column('price', sa.String(), nullable=True),
    sa.Column('to_redirect', sa.String(length=20), nullable=True),
    sa.Column('featured', sa.String(length=20), nullable=True),
    sa.Column('subject_title', sa.String(length=20), nullable=True),
    sa.Column('others1', sa.String(length=20), nullable=True),
    sa.Column('topic', sa.String(), nullable=True),
    sa.Column('others2', sa.String(length=20), nullable=True),
    sa.Column('time_limit1', sa.Integer(), nullable=True),
    sa.Column('time_limit2', sa.Integer(), nullable=True),
    sa.Column('url_slug', sa.String(length=255), nullable=True),
    sa.Column('grade', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('set',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('set')
    op.drop_table('post')
    # ### end Alembic commands ###

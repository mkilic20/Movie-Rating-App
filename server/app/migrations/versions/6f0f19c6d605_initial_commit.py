"""initial commit

Revision ID: 6f0f19c6d605
Revises: 
Create Date: 2023-08-07 22:10:22.655969

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f0f19c6d605'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'movie',
        sa.Column('MovieID', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('Name', sa.String(length=255), nullable=True),
        sa.Column('Year', sa.Integer(), nullable=True),
        sa.Column('Runtime', sa.Integer(), nullable=True),
        sa.Column('Rating', sa.Float(), nullable=True),
        sa.Column('Votes', sa.Integer(), nullable=True),
        sa.Column('Revenue', sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint('MovieID'),
        sa.UniqueConstraint('Name')
    )
    op.create_index(op.f('ix_movie_MovieID'), 'movie', ['MovieID'], unique=False)
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_table(
        'rating',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('movie_id', sa.Integer(), nullable=False),
        sa.Column('rating', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['movie_id'], ['movie.MovieID'], ),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_rating_id'), 'rating', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_rating_id'), table_name='rating')
    op.drop_table('rating')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_movie_MovieID'), table_name='movie')
    op.drop_table('movie')
    # ### end Alembic commands ###

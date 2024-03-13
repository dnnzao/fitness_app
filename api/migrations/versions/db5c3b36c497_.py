"""empty message

Revision ID: db5c3b36c497
Revises: ff21ddbcdc0d
Create Date: 2024-03-12 15:39:01.145131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db5c3b36c497'
down_revision = 'ff21ddbcdc0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_exercises')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_exercises',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('exercise_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['exercise_id'], ['exercises.id'], name='user_exercises_exercise_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='user_exercises_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='user_exercises_pkey')
    )
    # ### end Alembic commands ###
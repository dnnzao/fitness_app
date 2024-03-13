"""empty message

Revision ID: 5851f3298eab
Revises: a0c84a5777cc
Create Date: 2024-03-13 10:10:35.461875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5851f3298eab'
down_revision = 'a0c84a5777cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exercises', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exercises', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###

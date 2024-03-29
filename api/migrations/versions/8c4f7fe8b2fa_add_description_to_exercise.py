"""Add description to Exercise

Revision ID: 8c4f7fe8b2fa
Revises: 5851f3298eab
Create Date: 2024-03-13 11:05:04.435509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c4f7fe8b2fa'
down_revision = '5851f3298eab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exercises', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.Text(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exercises', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###

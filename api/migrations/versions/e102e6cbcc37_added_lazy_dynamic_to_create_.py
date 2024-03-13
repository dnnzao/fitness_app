"""Added lazy=dynamic to create interdependent tables

Revision ID: e102e6cbcc37
Revises: adb59a663a4a
Create Date: 2024-03-12 15:55:00.515646

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e102e6cbcc37'
down_revision = 'adb59a663a4a'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass

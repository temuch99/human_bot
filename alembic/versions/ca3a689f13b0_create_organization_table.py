"""create organization table

Revision ID: ca3a689f13b0
Revises: 87e5e5619268
Create Date: 2022-09-10 16:07:19.728966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca3a689f13b0'
down_revision = '87e5e5619268'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'human',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=True),
        sa.Column('type', sa.String(50), nullable=True),
        sa.Column('inn', sa.Integer, nullable=True),
        sa.Column('other', sa.Unicode(200))
    )


def downgrade():
    op.drop_table('human')

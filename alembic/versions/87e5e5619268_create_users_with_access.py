"""Create users with access

Revision ID: 87e5e5619268
Revises: fac98b5e67bf
Create Date: 2022-09-10 06:24:19.173219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87e5e5619268'
down_revision = 'fac98b5e67bf'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('telegram_id', sa.Integer, nullable=False)
    )


def downgrade():
    op.drop_table('user')

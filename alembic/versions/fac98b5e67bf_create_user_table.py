"""create user table

Revision ID: fac98b5e67bf
Revises: 
Create Date: 2022-08-28 17:06:11.683691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fac98b5e67bf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'human',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(50), nullable=True),
        sa.Column('last_name', sa.String(50), nullable=True),
        sa.Column('surname', sa.String(50), nullable=True),
        sa.Column('birthdate', sa.Date, nullable=True),
        sa.Column('other', sa.Unicode(200))
    )


def downgrade():
    op.drop_table('human')

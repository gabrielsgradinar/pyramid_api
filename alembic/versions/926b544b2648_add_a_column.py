"""Add a column

Revision ID: 926b544b2648
Revises: 72a39b47bcf6
Create Date: 2021-05-19 10:34:32.397167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '926b544b2648'
down_revision = '72a39b47bcf6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('countries', sa.Column('population', sa.BigInteger()))


def downgrade():
    op.drop_column('countries', 'population')

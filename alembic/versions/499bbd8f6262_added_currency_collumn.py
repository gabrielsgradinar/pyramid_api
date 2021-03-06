"""Added currency collumn

Revision ID: 499bbd8f6262
Revises: 926b544b2648
Create Date: 2021-05-19 16:01:03.332478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "499bbd8f6262"
down_revision = "926b544b2648"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("countries", sa.Column("currency", sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("countries", "currency")
    # ### end Alembic commands ###

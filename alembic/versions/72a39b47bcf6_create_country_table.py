"""create country table

Revision ID: 72a39b47bcf6
Revises:
Create Date: 2021-05-19 10:16:18.656786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "72a39b47bcf6"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "countries",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("official_language", sa.String()),
    )


def downgrade():
    op.drop_table("countries")

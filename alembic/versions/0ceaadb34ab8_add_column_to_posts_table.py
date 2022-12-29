"""add column to posts table

Revision ID: 0ceaadb34ab8
Revises: f845a2e60f7c
Create Date: 2022-12-26 10:17:45.884248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ceaadb34ab8'
down_revision = 'f845a2e60f7c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", 'content')
    pass

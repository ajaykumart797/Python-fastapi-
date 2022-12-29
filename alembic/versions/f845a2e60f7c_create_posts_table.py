"""create posts table

Revision ID: f845a2e60f7c
Revises: 
Create Date: 2022-12-25 11:21:47.604437

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f845a2e60f7c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # op.create_table("posts", sa.column("id", sa.Integer(),nullable=False), sa.column("title", sa.String()))
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False ))
    pass


def downgrade() -> None:
    op.drop_table("posts")
    pass

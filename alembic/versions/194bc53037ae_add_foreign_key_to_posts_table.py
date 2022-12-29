"""add foreign key to posts table

Revision ID: 194bc53037ae
Revises: 5e7b2324b075
Create Date: 2022-12-26 10:46:51.288952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '194bc53037ae'
down_revision = '5e7b2324b075'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
        'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass

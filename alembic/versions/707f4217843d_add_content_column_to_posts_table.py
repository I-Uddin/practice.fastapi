"""add content column to posts table

Revision ID: 707f4217843d
Revises: 6363b306c5cf
Create Date: 2022-10-22 23:00:44.234568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '707f4217843d'
down_revision = '6363b306c5cf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass

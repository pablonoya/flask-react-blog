"""Adding active field to Post model

Revision ID: e5ddf8a7257f
Revises: 267569508a2a
Create Date: 2021-04-16 10:19:52.642513

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e5ddf8a7257f'
down_revision = '267569508a2a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('active', sa.Boolean(), nullable=True))
    op.add_column('posts', sa.Column('img_url', sa.String(length=64), nullable=True))
    op.drop_column('posts', 'img')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('img', mysql.VARCHAR(collation='utf8_bin', length=64), nullable=True))
    op.drop_column('posts', 'img_url')
    op.drop_column('posts', 'active')
    # ### end Alembic commands ###

"""empty message

Revision ID: 1ba39e2641d8
Revises: fd7d1fbb7cce
Create Date: 2019-09-11 21:21:30.643027

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ba39e2641d8'
down_revision = 'fd7d1fbb7cce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_comments_float_id', table_name='comments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_comments_float_id', 'comments', ['float_id'], unique=False)
    # ### end Alembic commands ###

"""empty message

Revision ID: fd7d1fbb7cce
Revises: bb4df5b67283
Create Date: 2019-09-11 20:26:49.925932

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd7d1fbb7cce'
down_revision = 'bb4df5b67283'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('float_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_comments_float_id'), 'comments', ['float_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comments_float_id'), table_name='comments')
    op.drop_column('comments', 'float_id')
    # ### end Alembic commands ###
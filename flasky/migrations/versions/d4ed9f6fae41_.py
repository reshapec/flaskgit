"""empty message

Revision ID: d4ed9f6fae41
Revises: d2123919f84d
Create Date: 2019-09-09 13:07:25.155184

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4ed9f6fae41'
down_revision = 'd2123919f84d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('replys', sa.Column('from_user_id', sa.Integer(), nullable=True))
    op.add_column('replys', sa.Column('reply_type', sa.String(length=64), nullable=True))
    op.add_column('replys', sa.Column('to_user_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_replys_timestamp'), 'replys', ['timestamp'], unique=False)
    op.create_foreign_key(None, 'replys', 'users', ['from_user_id'], ['id'])
    op.create_foreign_key(None, 'replys', 'users', ['to_user_id'], ['id'])
    op.create_foreign_key(None, 'replys', 'comments', ['comment_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'replys', type_='foreignkey')
    op.drop_constraint(None, 'replys', type_='foreignkey')
    op.drop_constraint(None, 'replys', type_='foreignkey')
    op.drop_index(op.f('ix_replys_timestamp'), table_name='replys')
    op.drop_column('replys', 'to_user_id')
    op.drop_column('replys', 'reply_type')
    op.drop_column('replys', 'from_user_id')
    # ### end Alembic commands ###
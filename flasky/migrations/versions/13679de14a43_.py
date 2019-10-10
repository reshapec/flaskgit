"""empty message

Revision ID: 13679de14a43
Revises: 892daaf1f77b
Create Date: 2019-09-09 20:54:07.980327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13679de14a43'
down_revision = '892daaf1f77b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('parent_child',
    sa.Column('parent_id', sa.Integer(), nullable=False),
    sa.Column('child_id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['child_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['parent_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('parent_id', 'child_id')
    )
    op.drop_index('ix_replys_timestamp', table_name='replys')
    op.drop_table('replys')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('replys',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('body', sa.TEXT(), nullable=True),
    sa.Column('body_html', sa.TEXT(), nullable=True),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.Column('comment_id', sa.INTEGER(), nullable=True),
    sa.Column('reply_type', sa.BOOLEAN(), nullable=True),
    sa.Column('from_user_id', sa.INTEGER(), nullable=True),
    sa.Column('to_user_id', sa.INTEGER(), nullable=True),
    sa.CheckConstraint('reply_type IN (0, 1)'),
    sa.ForeignKeyConstraint(['comment_id'], ['comments.id'], ),
    sa.ForeignKeyConstraint(['from_user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['to_user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_replys_timestamp', 'replys', ['timestamp'], unique=False)
    op.drop_table('parent_child')
    # ### end Alembic commands ###

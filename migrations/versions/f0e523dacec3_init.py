"""init

Revision ID: f0e523dacec3
Revises: 
Create Date: 2019-07-30 08:32:40.890382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0e523dacec3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('bot',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slug', sa.String(length=16), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('name_customizable', sa.Boolean(), nullable=True),
    sa.Column('avatar_url', sa.String(length=70), nullable=True),
    sa.Column('avatar_url_customizable', sa.Boolean(), nullable=True),
    sa.Column('callback_url', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('bot_instance',
    sa.Column('group_id', sa.String(length=16), nullable=False),
    sa.Column('group_name', sa.String(length=50), nullable=True),
    sa.Column('bot_id', sa.String(length=26), nullable=True),
    sa.Column('owner_id', sa.String(length=16), nullable=True),
    sa.Column('owner_name', sa.String(length=64), nullable=True),
    sa.Column('access_token', sa.String(length=32), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['bot.id'], ),
    sa.PrimaryKeyConstraint('group_id'),
    sa.UniqueConstraint('bot_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bot_instance')
    op.drop_table('bot')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
"""empty message

Revision ID: 393eb0b01a27
Revises: 460febbda8b5
Create Date: 2019-09-20 21:41:13.976053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '393eb0b01a27'
down_revision = '460febbda8b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bot', sa.Column('prefix', sa.String(length=20), nullable=True))
    op.add_column('bot', sa.Column('test_group', sa.String(length=60), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bot', 'test_group')
    op.drop_column('bot', 'prefix')
    # ### end Alembic commands ###
"""empty message

Revision ID: beb517796058
Revises: 16e33986a325
Create Date: 2018-06-13 10:42:26.048460

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'beb517796058'
down_revision = '16e33986a325'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('telephone', table_name='front_user')
    op.drop_column('front_user', 'telephone')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('front_user', sa.Column('telephone', mysql.VARCHAR(length=11), nullable=False))
    op.create_index('telephone', 'front_user', ['telephone'], unique=True)
    # ### end Alembic commands ###

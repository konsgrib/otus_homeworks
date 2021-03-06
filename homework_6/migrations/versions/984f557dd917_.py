"""empty message

Revision ID: 984f557dd917
Revises: 396e0404cfb8
Create Date: 2022-06-01 22:48:59.469718

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '984f557dd917'
down_revision = '396e0404cfb8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###

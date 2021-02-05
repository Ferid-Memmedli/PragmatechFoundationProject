"""empty message

Revision ID: 78119de875df
Revises: 06c918aba81b
Create Date: 2021-02-02 16:02:08.854900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78119de875df'
down_revision = '06c918aba81b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('elaqe', sa.String(length=100), nullable=False),
    sa.Column('unvan', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contact')
    # ### end Alembic commands ###
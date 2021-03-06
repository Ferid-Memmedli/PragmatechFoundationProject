"""empty message

Revision ID: d27de90eeb59
Revises: 161521943d05
Create Date: 2021-02-04 19:44:44.532551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd27de90eeb59'
down_revision = '161521943d05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('social',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('link', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('social')
    # ### end Alembic commands ###

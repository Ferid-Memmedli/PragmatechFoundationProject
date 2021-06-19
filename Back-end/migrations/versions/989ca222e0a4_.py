"""empty message

Revision ID: 989ca222e0a4
Revises: db5368cdeaa7
Create Date: 2021-02-09 00:39:20.905944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '989ca222e0a4'
down_revision = 'db5368cdeaa7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
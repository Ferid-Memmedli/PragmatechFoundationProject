"""empty message

Revision ID: 3de6814c4ae9
Revises: 5ca72547f9d7
Create Date: 2021-02-02 23:39:43.440387

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3de6814c4ae9'
down_revision = '5ca72547f9d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('seo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('homeimage', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('seo', schema=None) as batch_op:
        batch_op.drop_column('homeimage')

    # ### end Alembic commands ###

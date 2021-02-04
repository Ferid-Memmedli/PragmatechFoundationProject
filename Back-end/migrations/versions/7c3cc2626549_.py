"""empty message

Revision ID: 7c3cc2626549
Revises: 3f3d84eae10b
Create Date: 2021-02-04 20:31:03.735505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c3cc2626549'
down_revision = '3f3d84eae10b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('social', schema=None) as batch_op:
        batch_op.alter_column('facebook',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('instagram',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('pinterest',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('twitter',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('social', schema=None) as batch_op:
        batch_op.alter_column('twitter',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('pinterest',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('instagram',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('facebook',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###

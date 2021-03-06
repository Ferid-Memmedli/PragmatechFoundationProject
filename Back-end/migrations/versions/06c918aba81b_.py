"""empty message

Revision ID: 06c918aba81b
Revises: 
Create Date: 2021-01-29 23:14:32.033673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06c918aba81b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blogs', schema=None) as batch_op:
        batch_op.alter_column('blogAuthor',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('blogDetail',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('blogImage',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('blogTitle',
               existing_type=sa.VARCHAR(),
               nullable=False)

    with op.batch_alter_table('form', schema=None) as batch_op:
        batch_op.alter_column('userEmail',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('userMessage',
               existing_type=sa.TEXT(),
               nullable=False)
        batch_op.alter_column('userName',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('userSubject',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('form', schema=None) as batch_op:
        batch_op.alter_column('userSubject',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('userName',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
        batch_op.alter_column('userMessage',
               existing_type=sa.TEXT(),
               nullable=True)
        batch_op.alter_column('userEmail',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)

    with op.batch_alter_table('blogs', schema=None) as batch_op:
        batch_op.alter_column('blogTitle',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('blogImage',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('blogDetail',
               existing_type=sa.TEXT(),
               nullable=True)
        batch_op.alter_column('blogAuthor',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###

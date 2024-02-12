"""+ phone_number field in customer_profile

Revision ID: d98b6078e70c
Revises: 7d939432c000
Create Date: 2024-02-12 09:38:00.172007

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd98b6078e70c'
down_revision = '7d939432c000'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('customer_profile', schema=None) as batch_op:
        batch_op.add_column(sa.Column('phone_number', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('customer_profile', schema=None) as batch_op:
        batch_op.drop_column('phone_number')

    # ### end Alembic commands ###

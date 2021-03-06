"""empty message

Revision ID: 2d2fc3e826af
Revises: 5e868298fee7
Create Date: 2019-12-09 22:40:03.692555

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d2fc3e826af'
down_revision = '5e868298fee7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('forward_email', sa.Column('website_from', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('forward_email', 'website_from')
    # ### end Alembic commands ###

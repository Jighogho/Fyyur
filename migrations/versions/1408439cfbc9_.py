"""empty message

Revision ID: 1408439cfbc9
Revises: 7d078f372135
Create Date: 2022-06-04 14:52:40.601466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1408439cfbc9'
down_revision = '7d078f372135'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'Artist', ['id'])
    op.create_unique_constraint(None, 'Show', ['id'])
    op.create_unique_constraint(None, 'Venue', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Venue', type_='unique')
    op.drop_constraint(None, 'Show', type_='unique')
    op.drop_constraint(None, 'Artist', type_='unique')
    # ### end Alembic commands ###

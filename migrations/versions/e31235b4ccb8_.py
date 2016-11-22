"""empty message

Revision ID: e31235b4ccb8
Revises: 5078997cb6c6
Create Date: 2016-11-22 01:47:08.084153

"""

# revision identifiers, used by Alembic.
revision = 'e31235b4ccb8'
down_revision = '5078997cb6c6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_RiverStation_location_code', table_name='RiverStation')
    op.drop_column('RiverStation', 'location_code')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('RiverStation', sa.Column('location_code', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_index('ix_RiverStation_location_code', 'RiverStation', ['location_code'], unique=True)
    ### end Alembic commands ###

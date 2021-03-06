"""empty message

Revision ID: 4d04ae7f5ece
Revises: None
Create Date: 2016-10-29 19:23:25.754960

"""

# revision identifiers, used by Alembic.
revision = '4d04ae7f5ece'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('office', sa.String(length=64), nullable=True),
    sa.Column('station_name', sa.String(length=64), nullable=True),
    sa.Column('location_code', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('office')
    )
    op.create_index(op.f('ix_stations_location_code'), 'stations', ['location_code'], unique=True)
    op.create_index(op.f('ix_stations_station_name'), 'stations', ['station_name'], unique=True)
    op.create_table('measurments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('station_id', sa.Integer(), nullable=True),
    sa.Column('date_time', sa.DateTime(), nullable=True),
    sa.Column('value', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['station_id'], ['stations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('measurments')
    op.drop_index(op.f('ix_stations_station_name'), table_name='stations')
    op.drop_index(op.f('ix_stations_location_code'), table_name='stations')
    op.drop_table('stations')
    ### end Alembic commands ###

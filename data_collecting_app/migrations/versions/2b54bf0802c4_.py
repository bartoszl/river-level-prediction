"""empty message

Revision ID: 2b54bf0802c4
Revises: 8f800a63242f
Create Date: 2016-12-01 14:07:48.707841

"""

# revision identifiers, used by Alembic.
revision = '2b54bf0802c4'
down_revision = '8f800a63242f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('CurrentWeather', sa.Column('description', sa.String(length=256), nullable=False))
    op.add_column('CurrentWeather', sa.Column('temperature', sa.Float(), nullable=False))
    op.add_column('CurrentWeather', sa.Column('wind_direction', sa.Float(), nullable=False))
    op.add_column('CurrentWeather', sa.Column('wind_speed', sa.Float(), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('CurrentWeather', 'wind_speed')
    op.drop_column('CurrentWeather', 'wind_direction')
    op.drop_column('CurrentWeather', 'temperature')
    op.drop_column('CurrentWeather', 'description')
    ### end Alembic commands ###

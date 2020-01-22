"""empty message

Revision ID: 78acaef46db6
Revises: 90a23202028e
Create Date: 2020-01-18 21:18:53.320821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78acaef46db6'
down_revision = '90a23202028e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('forecast',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('coord_lon', sa.Float(), nullable=True),
    sa.Column('coord_lat', sa.Float(), nullable=True),
    sa.Column('positive', sa.Boolean(), nullable=True),
    sa.Column('weather_id', sa.Integer(), nullable=True),
    sa.Column('weather_main', sa.String(length=200), nullable=True),
    sa.Column('weather_description', sa.String(length=200), nullable=True),
    sa.Column('weather_icon', sa.String(length=200), nullable=True),
    sa.Column('base', sa.String(length=200), nullable=True),
    sa.Column('main_temp', sa.Float(), nullable=True),
    sa.Column('main_feels_like', sa.Float(), nullable=True),
    sa.Column('main_temp_min', sa.Float(), nullable=True),
    sa.Column('main_temp_max', sa.Float(), nullable=True),
    sa.Column('main_pressure', sa.Integer(), nullable=True),
    sa.Column('main_humidity', sa.Integer(), nullable=True),
    sa.Column('main_sea_level', sa.Integer(), nullable=True),
    sa.Column('main_grnd_level', sa.Integer(), nullable=True),
    sa.Column('visibility', sa.Integer(), nullable=True),
    sa.Column('wind_speed', sa.Float(), nullable=True),
    sa.Column('wind_deg', sa.Integer(), nullable=True),
    sa.Column('clouds_all', sa.Integer(), nullable=True),
    sa.Column('rain_1h', sa.Float(), nullable=True),
    sa.Column('rain_3h', sa.Float(), nullable=True),
    sa.Column('snow_1h', sa.Float(), nullable=True),
    sa.Column('snow_3h', sa.Float(), nullable=True),
    sa.Column('dt', sa.Integer(), nullable=True),
    sa.Column('sys_type', sa.Integer(), nullable=True),
    sa.Column('sys_id', sa.Integer(), nullable=True),
    sa.Column('sys_message', sa.String(length=200), nullable=True),
    sa.Column('sys_country', sa.String(length=200), nullable=True),
    sa.Column('sys_sunrise', sa.Integer(), nullable=True),
    sa.Column('sys_sunset', sa.Integer(), nullable=True),
    sa.Column('timezone', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('cod', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('forecast')
    # ### end Alembic commands ###

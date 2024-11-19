"""Inisial

Revision ID: fda5c4dc570c
Revises: 
Create Date: 2024-11-19 14:33:50.262646

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fda5c4dc570c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fakultas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nama', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fakultas')
    # ### end Alembic commands ###

"""empty message

Revision ID: 63ff96644987
Revises: 
Create Date: 2022-08-31 17:22:31.456424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63ff96644987'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fname', sa.String(length=24), nullable=False),
    sa.Column('lname', sa.String(length=24), nullable=False),
    sa.Column('email', sa.String(length=160), nullable=False),
    sa.Column('password_hash', sa.String(length=200), nullable=False),
    sa.Column('gender', sa.Integer(), nullable=False),
    sa.Column('role', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
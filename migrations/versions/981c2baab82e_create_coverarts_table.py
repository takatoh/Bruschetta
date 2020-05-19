"""Create coverarts table

Revision ID: 981c2baab82e
Revises: 0bff8cd02ef3
Create Date: 2020-05-19 18:29:44.148828

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '981c2baab82e'
down_revision = '0bff8cd02ef3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coverarts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('books', sa.Column('coverart_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'books', 'coverarts', ['coverart_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'books', type_='foreignkey')
    op.drop_column('books', 'coverart_id')
    op.drop_table('coverarts')
    # ### end Alembic commands ###

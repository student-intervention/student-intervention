"""document table

Revision ID: 77f3b93307cf
Revises: 77a05619f130
Create Date: 2018-08-26 18:51:33.809000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77f3b93307cf'
down_revision = '77a05619f130'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('document',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fname', sa.String(length=120), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_document_fname'), 'document', ['fname'], unique=False)
    op.create_index(op.f('ix_document_timestamp'), 'document', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_document_timestamp'), table_name='document')
    op.drop_index(op.f('ix_document_fname'), table_name='document')
    op.drop_table('document')
    # ### end Alembic commands ###
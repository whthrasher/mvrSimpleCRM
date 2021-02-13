"""empty message

Revision ID: c55a11694f27
Revises: c86cdd833757
Create Date: 2021-02-12 20:59:44.121626

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c55a11694f27'
down_revision = 'c86cdd833757'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('membership_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('member_relationships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=False),
    sa.Column('business_id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('membership_type', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['business_id'], ['businesses.id'], ),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], ),
    sa.ForeignKeyConstraint(['membership_type'], ['membership_types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('customer_relationships')
    op.drop_column('members', 'membership_type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('members', sa.Column('membership_type', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.create_table('customer_relationships',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('date_added', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('business_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('member_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('membership_type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['business_id'], ['businesses.id'], name='customer_relationships_business_id_fkey'),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], name='customer_relationships_member_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='customer_relationships_pkey')
    )
    op.drop_table('member_relationships')
    op.drop_table('membership_types')
    # ### end Alembic commands ###

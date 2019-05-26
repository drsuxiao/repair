"""empty message

Revision ID: 8bed969b36c5
Revises: 
Create Date: 2019-05-24 23:34:33.042201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bed969b36c5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=10), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_department_code'), 'department', ['code'], unique=True)
    op.create_index(op.f('ix_department_name'), 'department', ['name'], unique=True)
    op.create_table('equipment_brand',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=10), nullable=True),
    sa.Column('name', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_equipment_brand_code'), 'equipment_brand', ['code'], unique=True)
    op.create_index(op.f('ix_equipment_brand_name'), 'equipment_brand', ['name'], unique=True)
    op.create_table('equipment_fault',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=10), nullable=True),
    sa.Column('name', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_equipment_fault_code'), 'equipment_fault', ['code'], unique=True)
    op.create_index(op.f('ix_equipment_fault_name'), 'equipment_fault', ['name'], unique=True)
    op.create_table('equipment_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=10), nullable=True),
    sa.Column('name', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_equipment_type_code'), 'equipment_type', ['code'], unique=True)
    op.create_index(op.f('ix_equipment_type_name'), 'equipment_type', ['name'], unique=True)
    op.create_table('repair_company',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=10), nullable=True),
    sa.Column('name', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_repair_company_code'), 'repair_company', ['code'], unique=True)
    op.create_index(op.f('ix_repair_company_name'), 'repair_company', ['name'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usercode', sa.String(length=10), nullable=True),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_usercode'), 'users', ['usercode'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    op.create_table('equipment_repair',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('repair_date', sa.DateTime(), nullable=True),
    sa.Column('dept_code', sa.String(length=10), nullable=True),
    sa.Column('repair_registrant', sa.String(length=10), nullable=True),
    sa.Column('brand_code', sa.String(length=10), nullable=True),
    sa.Column('type_code', sa.String(length=10), nullable=True),
    sa.Column('equipment_code', sa.String(length=10), nullable=True),
    sa.Column('fault_code', sa.String(length=10), nullable=True),
    sa.Column('com_code', sa.String(length=10), nullable=True),
    sa.Column('repair_man', sa.String(length=10), nullable=True),
    sa.Column('repair_return_date', sa.DateTime(), nullable=True),
    sa.Column('repair_return_man', sa.String(length=10), nullable=True),
    sa.Column('equipment_return_date', sa.DateTime(), nullable=True),
    sa.Column('equipment_return_man', sa.String(length=10), nullable=True),
    sa.Column('repair_status', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['brand_code'], ['equipment_brand.code'], ),
    sa.ForeignKeyConstraint(['com_code'], ['repair_company.code'], ),
    sa.ForeignKeyConstraint(['dept_code'], ['department.code'], ),
    sa.ForeignKeyConstraint(['fault_code'], ['equipment_fault.code'], ),
    sa.ForeignKeyConstraint(['type_code'], ['equipment_type.code'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('equipment_repair')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_usercode'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_repair_company_name'), table_name='repair_company')
    op.drop_index(op.f('ix_repair_company_code'), table_name='repair_company')
    op.drop_table('repair_company')
    op.drop_index(op.f('ix_equipment_type_name'), table_name='equipment_type')
    op.drop_index(op.f('ix_equipment_type_code'), table_name='equipment_type')
    op.drop_table('equipment_type')
    op.drop_index(op.f('ix_equipment_fault_name'), table_name='equipment_fault')
    op.drop_index(op.f('ix_equipment_fault_code'), table_name='equipment_fault')
    op.drop_table('equipment_fault')
    op.drop_index(op.f('ix_equipment_brand_name'), table_name='equipment_brand')
    op.drop_index(op.f('ix_equipment_brand_code'), table_name='equipment_brand')
    op.drop_table('equipment_brand')
    op.drop_index(op.f('ix_department_name'), table_name='department')
    op.drop_index(op.f('ix_department_code'), table_name='department')
    op.drop_table('department')
    # ### end Alembic commands ###
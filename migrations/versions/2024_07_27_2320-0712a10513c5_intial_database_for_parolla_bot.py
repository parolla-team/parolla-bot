"""intial database for parolla bot

Revision ID: 0712a10513c5
Revises: 
Create Date: 2024-07-27 23:20:15.065814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0712a10513c5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('guid', sa.String(), nullable=False),
        sa.Column('platform_user_id', sa.String(length=255), nullable=False),
        sa.Column('platform_private_channel_id', sa.String(length=255), nullable=False),
        sa.Column('platform_name', sa.String(length=255), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('username', sa.String(length=90), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'profiles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('learning_frequency', sa.String(length=255), nullable=False),
        sa.Column('language_region', sa.String(length=255), nullable=False),
        sa.Column('global_feedback', sa.Text(), nullable=False),
        sa.Column('learning_methodology', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['users.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'sessions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('guid', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('description', sa.String(length=255), nullable=True),
        sa.Column('platform_channel_id', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['users.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'interactions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('session_id', sa.Integer(), nullable=False),
        sa.Column('author', sa.String(length=255), nullable=False),
        sa.Column('text', sa.Text(), nullable=False),
        sa.Column('platform_message_id', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ['session_id'],
            ['sessions.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'roadmaps',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('profile_id', sa.Integer(), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ['profile_id'],
            ['profiles.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roadmaps')
    op.drop_table('interactions')
    op.drop_table('sessions')
    op.drop_table('profiles')
    op.drop_table('users')
    # ### end Alembic commands ###

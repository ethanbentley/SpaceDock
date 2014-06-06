"""Add mods and media

Revision ID: 2ef141f5132
Revises: 1fb18596264
Create Date: 2014-06-06 00:00:28.128296

"""

# revision identifiers, used by Alembic.
revision = '2ef141f5132'
down_revision = '1fb18596264'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_mods')
    op.drop_table('mod_media')
    op.add_column('media', sa.Column('mod_id', sa.Integer(), nullable=True))
    op.add_column('mod', sa.Column('approved', sa.Boolean(), nullable=True))
    op.add_column('mod', sa.Column('created', sa.DateTime(), nullable=True))
    op.add_column('mod', sa.Column('description', sa.Unicode(length=100000), nullable=True))
    op.add_column('mod', sa.Column('donation_link', sa.String(length=128), nullable=True))
    op.add_column('mod', sa.Column('external_link', sa.String(length=128), nullable=True))
    op.add_column('mod', sa.Column('installation', sa.Unicode(length=100000), nullable=True))
    op.add_column('mod', sa.Column('keywords', sa.String(length=256), nullable=True))
    op.add_column('mod', sa.Column('license', sa.String(length=128), nullable=True))
    op.add_column('mod', sa.Column('published', sa.Boolean(), nullable=True))
    op.add_column('mod', sa.Column('user_id', sa.Integer(), nullable=True))
    op.add_column('mod', sa.Column('votes', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('mod', 'votes')
    op.drop_column('mod', 'user_id')
    op.drop_column('mod', 'published')
    op.drop_column('mod', 'license')
    op.drop_column('mod', 'keywords')
    op.drop_column('mod', 'installation')
    op.drop_column('mod', 'external_link')
    op.drop_column('mod', 'donation_link')
    op.drop_column('mod', 'description')
    op.drop_column('mod', 'created')
    op.drop_column('mod', 'approved')
    op.drop_column('media', 'mod_id')
    op.create_table('mod_media',
    sa.Column('media_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('mod_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['media_id'], ['media.id'], name='mod_media_media_id_fkey'),
    sa.ForeignKeyConstraint(['mod_id'], ['mod.id'], name='mod_media_mod_id_fkey')
    )
    op.create_table('user_mods',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('mod_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['mod_id'], ['mod.id'], name='user_mods_mod_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='user_mods_user_id_fkey')
    )
    ### end Alembic commands ###

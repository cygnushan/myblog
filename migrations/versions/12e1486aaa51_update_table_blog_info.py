"""update table blog_info

Revision ID: 12e1486aaa51
Revises: 069c4b97de5b
Create Date: 2017-06-08 09:16:27.658000

"""

# revision identifiers, used by Alembic.
revision = '12e1486aaa51'
down_revision = '069c4b97de5b'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_info', sa.Column('editor', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog_info', 'editor')
    op.drop_constraint(None, 'articles', type_='foreignkey')
    op.create_foreign_key(u'articles_ibfk_1', 'articles', 'articletypes', ['articleType_id'], ['id'])
    op.create_table('articletypes',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('introduction', mysql.TEXT(), nullable=True),
    sa.Column('menu_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('setting_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['menu_id'], [u'menus.id'], name=u'articletypes_ibfk_1'),
    sa.ForeignKeyConstraint(['setting_id'], [u'articletypesettings.id'], name=u'articletypes_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('articletypesettings',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=64), nullable=True),
    sa.Column('protected', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('hide', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.drop_table('articleTypes')
    op.drop_table('articleTypeSettings')
    # ### end Alembic commands ###
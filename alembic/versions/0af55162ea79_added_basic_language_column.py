"""Added basic_language column

Revision ID: 0af55162ea79
Revises: 
Create Date: 2023-12-15 11:40:47.519593

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '0af55162ea79'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_email', table_name='user')
    op.drop_table('user')
    op.drop_index('ix_user_assistant_assistant_id', table_name='user_assistant')
    op.drop_index('ix_user_assistant_user_id', table_name='user_assistant')
    op.drop_table('user_assistant')
    op.add_column('assistant', sa.Column('basic_language', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('assistant', 'basic_language')
    op.create_table('user_assistant',
    sa.Column('user_id', mysql.CHAR(length=32), nullable=False),
    sa.Column('assistant_id', mysql.CHAR(length=32), nullable=False),
    sa.Column('createTime', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updateTime', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('user_id', 'assistant_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_user_assistant_user_id', 'user_assistant', ['user_id'], unique=False)
    op.create_index('ix_user_assistant_assistant_id', 'user_assistant', ['assistant_id'], unique=False)
    op.create_table('user',
    sa.Column('id', mysql.CHAR(length=36), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=320), nullable=False),
    sa.Column('hashed_password', mysql.VARCHAR(length=1024), nullable=False),
    sa.Column('is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.Column('is_superuser', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.Column('is_verified', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_user_email', 'user', ['email'], unique=False)
    # ### end Alembic commands ###

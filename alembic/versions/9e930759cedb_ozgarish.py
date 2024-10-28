"""ozgarish

Revision ID: 9e930759cedb
Revises: e1fbd32f44de
Create Date: 2024-10-28 20:10:55.798033

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9e930759cedb'
down_revision: Union[str, None] = 'e1fbd32f44de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('user_name', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'user_name')
    # ### end Alembic commands ###

"""empty message

Revision ID: 0590d6ce91b6
Revises: 0555d5e1be2b
Create Date: 2024-07-06 10:49:53.388959

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0590d6ce91b6'
down_revision: Union[str, None] = '0555d5e1be2b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('animal', sa.Column('production', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('animal', 'production')
    # ### end Alembic commands ###

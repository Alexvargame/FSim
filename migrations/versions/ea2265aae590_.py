"""empty message

Revision ID: ea2265aae590
Revises: 0c037bac2199
Create Date: 2024-06-30 11:55:07.348266

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ea2265aae590'
down_revision: Union[str, None] = '0c037bac2199'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('animal_type', sa.Column('capacity', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('animal_type', 'capacity')
    # ### end Alembic commands ###

"""fusion_migraciones

Revision ID: ec6339292a78
Revises: 0c7c0756f42c, b74c0c44479c
Create Date: 2025-04-08 12:51:09.803171

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ec6339292a78'
down_revision: Union[str, None] = ('0c7c0756f42c', 'b74c0c44479c')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

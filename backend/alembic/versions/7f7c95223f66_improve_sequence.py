"""Improve Sequence

Revision ID: 7f7c95223f66
Revises: 8aac4fca1372
Create Date: 2024-10-27 23:49:17.849366

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f7c95223f66'
down_revision: Union[str, None] = '8aac4fca1372'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
ALTER SEQUENCE contacts_id_seq
RESTART 2;
    
ALTER SEQUENCE main_article_id_seq
RESTART 34;

ALTER SEQUENCE news_id_seq
RESTART 37;

ALTER SEQUENCE partners_id_seq
RESTART 4;

ALTER SEQUENCE users_id_seq
RESTART 6;
    """)


def downgrade() -> None:
    op.execute(
        """
ALTER SEQUENCE news_id_seq
RESTART 1;

ALTER SEQUENCE contacts_id_seq
RESTART 1;

ALTER SEQUENCE main_article_id_seq
RESTART 1;

ALTER SEQUENCE partners_id_seq
RESTART 1;

ALTER SEQUENCE users_id_seq
RESTART 1;
        """
    )

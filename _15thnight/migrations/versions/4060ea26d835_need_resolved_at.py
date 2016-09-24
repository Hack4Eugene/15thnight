"""need resolved at

Revision ID: 4060ea26d835
Revises: 15d569ccbee5
Create Date: 2016-09-20 11:41:17.453728

"""

# revision identifiers, used by Alembic.
revision = '4060ea26d835'
down_revision = '15d569ccbee5'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('need', sa.Column('resolved_at', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('need', 'resolved_at')
    ### end Alembic commands ###

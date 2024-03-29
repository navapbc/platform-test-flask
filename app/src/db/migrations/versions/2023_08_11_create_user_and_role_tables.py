"""create user and role tables

Revision ID: 4ff1160282d1
Revises: 3ed861176e3d
Create Date: 2023-08-11 18:42:20.929289

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "4ff1160282d1"
down_revision = "3ed861176e3d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("first_name", sa.Text(), nullable=False),
        sa.Column("middle_name", sa.Text(), nullable=True),
        sa.Column("last_name", sa.Text(), nullable=False),
        sa.Column("phone_number", sa.Text(), nullable=False),
        sa.Column("date_of_birth", sa.Date(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("user_pkey")),
    )
    op.create_table(
        "role",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column(
            "type", sa.Enum("USER", "ADMIN", name="roletype", native_enum=False), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["user.id"], name=op.f("role_user_id_user_fkey"), ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("user_id", "type", name=op.f("role_pkey")),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("role")
    op.drop_table("user")
    # ### end Alembic commands ###

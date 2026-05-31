"""initial schema

Revision ID: a054a5b9362d
Revises:
Create Date: 2026-05-31 16:08:52.284965

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a054a5b9362d"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        "import_runs",
        sa.Column("import_run_id", sa.Integer(), nullable=False),
        sa.Column("source", sa.String(length=255), nullable=False),
        sa.Column("file_name", sa.String(length=255), nullable=False),
        sa.Column("record_count", sa.Integer(), nullable=False),
        sa.Column("licence", sa.String(length=255), nullable=True),
        sa.Column("retrieved_date", sa.String(length=100), nullable=True),
        sa.Column(
            "imported_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("import_run_id"),
    )

    op.create_index(
        op.f("ix_import_runs_import_run_id"),
        "import_runs",
        ["import_run_id"],
        unique=False,
    )

    op.create_table(
        "indicators",
        sa.Column("indicator_id", sa.Integer(), nullable=False),
        sa.Column("code", sa.String(length=50), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("unit", sa.String(length=50), nullable=True),
        sa.Column("source_system", sa.String(length=100), nullable=True),
        sa.PrimaryKeyConstraint("indicator_id"),
        sa.UniqueConstraint("code"),
    )

    op.create_index(
        op.f("ix_indicators_indicator_id"),
        "indicators",
        ["indicator_id"],
        unique=False,
    )

    op.create_table(
        "regions",
        sa.Column("region_id", sa.Integer(), nullable=False),
        sa.Column("ags", sa.String(length=20), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("level", sa.String(length=50), nullable=False),
        sa.Column("parent_region_id", sa.Integer(), nullable=True),
        sa.Column("population", sa.Integer(), nullable=True),
        sa.Column("area_km2", sa.Float(), nullable=True),
        sa.Column("longitude", sa.Float(), nullable=True),
        sa.Column("latitude", sa.Float(), nullable=True),
        sa.ForeignKeyConstraint(
            ["parent_region_id"],
            ["regions.region_id"],
        ),
        sa.PrimaryKeyConstraint("region_id"),
    )

    op.create_index(
        op.f("ix_regions_ags"),
        "regions",
        ["ags"],
        unique=True,
    )

    op.create_index(
        op.f("ix_regions_region_id"),
        "regions",
        ["region_id"],
        unique=False,
    )

    op.create_table(
        "source_metadata",
        sa.Column("source_id", sa.Integer(), nullable=False),
        sa.Column("source_name", sa.String(length=255), nullable=False),
        sa.Column("source_url", sa.String(length=500), nullable=True),
        sa.Column("licence_name", sa.String(length=255), nullable=True),
        sa.Column("licence_url", sa.String(length=500), nullable=True),
        sa.Column("retrieved_date", sa.String(length=100), nullable=True),
        sa.PrimaryKeyConstraint("source_id"),
    )

    op.create_index(
        op.f("ix_source_metadata_source_id"),
        "source_metadata",
        ["source_id"],
        unique=False,
    )

    op.create_table(
        "accidents",
        sa.Column("accident_id", sa.Integer(), nullable=False),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column("month", sa.Integer(), nullable=True),
        sa.Column("hour", sa.Integer(), nullable=True),
        sa.Column("weekday", sa.Integer(), nullable=True),
        sa.Column("category", sa.Integer(), nullable=True),
        sa.Column("type", sa.Integer(), nullable=True),
        sa.Column("light", sa.Integer(), nullable=True),
        sa.Column("ist_rad", sa.Integer(), nullable=True),
        sa.Column("ist_pkw", sa.Integer(), nullable=True),
        sa.Column("ist_fuss", sa.Integer(), nullable=True),
        sa.Column("ist_krad", sa.Integer(), nullable=True),
        sa.Column("ist_gkfz", sa.Integer(), nullable=True),
        sa.Column("longitude", sa.Float(), nullable=True),
        sa.Column("latitude", sa.Float(), nullable=True),
        sa.Column("region_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["region_id"],
            ["regions.region_id"],
        ),
        sa.PrimaryKeyConstraint("accident_id"),
    )

    op.create_index(
        op.f("ix_accidents_accident_id"),
        "accidents",
        ["accident_id"],
        unique=False,
    )

    op.create_index(
        op.f("ix_accidents_region_id"),
        "accidents",
        ["region_id"],
        unique=False,
    )

    op.create_index(
        op.f("ix_accidents_year"),
        "accidents",
        ["year"],
        unique=False,
    )

    op.create_table(
        "indicator_values",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("region_id", sa.Integer(), nullable=False),
        sa.Column("indicator_id", sa.Integer(), nullable=False),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column("value", sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(
            ["indicator_id"],
            ["indicators.indicator_id"],
        ),
        sa.ForeignKeyConstraint(
            ["region_id"],
            ["regions.region_id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        op.f("ix_indicator_values_id"),
        "indicator_values",
        ["id"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_index(
        op.f("ix_indicator_values_id"),
        table_name="indicator_values",
    )
    op.drop_table("indicator_values")

    op.drop_index(
        op.f("ix_accidents_year"),
        table_name="accidents",
    )
    op.drop_index(
        op.f("ix_accidents_region_id"),
        table_name="accidents",
    )
    op.drop_index(
        op.f("ix_accidents_accident_id"),
        table_name="accidents",
    )
    op.drop_table("accidents")

    op.drop_index(
        op.f("ix_source_metadata_source_id"),
        table_name="source_metadata",
    )
    op.drop_table("source_metadata")

    op.drop_index(
        op.f("ix_regions_region_id"),
        table_name="regions",
    )
    op.drop_index(
        op.f("ix_regions_ags"),
        table_name="regions",
    )
    op.drop_table("regions")

    op.drop_index(
        op.f("ix_indicators_indicator_id"),
        table_name="indicators",
    )
    op.drop_table("indicators")

    op.drop_index(
        op.f("ix_import_runs_import_run_id"),
        table_name="import_runs",
    )
    op.drop_table("import_runs")
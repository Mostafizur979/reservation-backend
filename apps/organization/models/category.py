from django.db import models

from apps.common.models.base import SoftDeleteModel
from apps.organization.models.section import Section


class RoomCategory(SoftDeleteModel):

    section = models.ForeignKey(
        Section,
        on_delete=models.PROTECT,
        related_name="room_categories",
    )

    name = models.CharField(
        max_length=100,
        db_index=True,
    )

    base_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    max_adult = models.PositiveIntegerField(
        default=1,
    )

    max_child = models.PositiveIntegerField(
        default=0,
    )

    bed_type = models.CharField(
        max_length=100,
        blank=True,
        default="",
    )

    description = models.TextField(
        blank=True,
        default="",
    )

    is_active = models.BooleanField(
        default=True,
        db_index=True,
    )

    class Meta:
        db_table = "room_categories"
        ordering = ["name"]

    def __str__(self):
        return self.name
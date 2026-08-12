from django.db import models

from apps.common.models.base import SoftDeleteModel
from apps.organization.models.category import RoomCategory


class Image(SoftDeleteModel):

    room_category = models.ForeignKey(
        RoomCategory,
        on_delete=models.CASCADE,
        related_name="images",
    )

    image = models.ImageField(
        upload_to="room-categories/",
        max_length=500,
    )

    is_primary = models.BooleanField(
        default=False,
    )

    display_order = models.PositiveIntegerField(
        default=0,
    )

    class Meta:
        db_table = "images"
        ordering = ["display_order", "id"]

    def __str__(self):
        return f"{self.room_category.name} - Image"
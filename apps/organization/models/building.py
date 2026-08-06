from django.db import models

from apps.common.models.base import SoftDeleteModel


class Building(SoftDeleteModel):
    code = models.CharField(
        max_length=20,
        unique=True,
        db_index=True,
    )

    name = models.CharField(
        max_length=150,
        db_index=True,
    )

    description = models.TextField(
        blank=True,
        default="",
    )

    class Meta:
        db_table = "organization_buildings"
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["code"]),
        ]

    def __str__(self):
        return self.name
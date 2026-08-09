from apps.common.models.base import SoftDeleteModel
from django.db import models 
from apps.organization.models.building import Building

class Floor(SoftDeleteModel):
    name = models.CharField(max_length=200, unique=True, null = False)
    number = models.IntegerField(null = False)
    code = models.CharField(max_length=30, unique=True, null = False)
    description = models.TextField(null = True)
    building = models.ForeignKey(
        Building,
        null=False,
        on_delete=models.PROTECT,
        related_name="floors",
    )
    class Meta:
        db_table = "building_floors"
        ordering = ["name", "number"]

    def __str__(self):
        return self.name    
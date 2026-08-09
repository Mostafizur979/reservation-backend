from apps.common.models.base import SoftDeleteModel
from apps.organization.models import Floor
from django.db import models

class Section(SoftDeleteModel):
    name = models.CharField(max_length=150, null=False)
    code = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True)
    floor = models.ForeignKey(
        Floor,
        null=False,
        on_delete=models.PROTECT,
        related_name="floor_sections",
    )

    class Meta:
        db_table = "floor_sections"
        ordering=['name']

    def __str__(self):
        return self.name
    


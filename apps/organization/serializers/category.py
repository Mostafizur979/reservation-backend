
from apps.organization.models.category import RoomCategory
from rest_framework import serializers
from apps.organization.serializers.image import ImageSerializer

class RoomCategorySerializer(serializers.ModelSerializer):

    images = ImageSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = RoomCategory

        fields = (
            "id",
            "section",
            "name",
            "base_price",
            "max_adult",
            "max_child",
            "bed_type",
            "description",
            "is_active",
            "images",
        )
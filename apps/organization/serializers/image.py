from rest_framework import serializers
from apps.organization.models.image import Image


class ImageSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = (
            "id",
            "room_category",
            "image",
            "is_primary",
            "display_order",
        )

        read_only_fields = (
            "id",
        )

    def get_image(self, obj):
        return str(obj.image) if obj.image else None
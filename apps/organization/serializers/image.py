from rest_framework import serializers
from apps.organization.models.image import Image
from apps.common.serializers.fields import R2ImageField

class ImageSerializer(serializers.ModelSerializer):

    image = R2ImageField(
        required=False,
        allow_null=True,
    )
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
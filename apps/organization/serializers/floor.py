from rest_framework import serializers

from apps.organization.models import Floor


class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = "__all__"

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
            "deleted_at",
            "deleted_by",
            "is_deleted",
            "orgunit_id",
        )

    def validate_code(self, value):
        qs = Floor.objects.filter(code__iexact=value)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise serializers.ValidationError(
                "Floor code already exists."
            )

        return value.strip().upper()

    def validate_name(self, value):
        qs = Floor.objects.filter(name__iexact=value)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise serializers.ValidationError(
                "Floor name already exists."
            )

        return value.strip()
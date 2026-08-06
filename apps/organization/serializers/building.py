from rest_framework import serializers
from apps.organization.models import Building
from apps.organization.models import Building


class BuildingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Building
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
        )

    def validate_code(self, value):
        qs = Building.objects.filter(code__iexact=value)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise serializers.ValidationError(
                "Building code already exists."
            )

        return value.upper()

    def validate_name(self, value):
        qs = Building.objects.filter(name__iexact=value)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise serializers.ValidationError(
                "Building name already exists."
            )

        return value.strip()
from rest_framework import serializers
from apps.organization.models import Section

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
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
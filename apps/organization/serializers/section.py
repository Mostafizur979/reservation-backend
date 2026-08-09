from rest_framework import serializers
from apps.organization.models import Section
from apps.common.api.read_only_fields import ReadOnlyFields
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"
        read_only_fields = ReadOnlyFields()

    def validate_code(self, value):
        qs = Section.objects.filter(code__iexact=value)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise serializers.ValidationError(
                "Section code already exists."
            )

        return value.strip().upper()
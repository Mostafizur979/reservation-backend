import django_filters

from apps.organization.models import Building


class BuildingFilter(django_filters.FilterSet):
    class Meta:
        model = Building
        fields = {
            "is_active": ["exact"],
        }
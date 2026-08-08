import django_filters
from apps.organization.models.floor import Floor

class FloorFilter(django_filters.FilterSet):
    class Meta:
        model = Floor
        fields = {
            "is_active": ["exact"],
            "building": ["exact"]
        }
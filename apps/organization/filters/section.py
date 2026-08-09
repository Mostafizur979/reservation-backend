from django_filters import FilterSet
from apps.organization.models.section import Section
class SectionFilter(FilterSet):
    class Meta:
        model = Section
        fields = {
            "orgunit_id" : ["exact"],
            "floor" : ["exact"]
        }
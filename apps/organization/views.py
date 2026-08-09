from apps.common.api.mixins import BaseModelViewSet

#Filter
from apps.organization.filters import BuildingFilter, FloorFilter, SectionFilter

#Model
from apps.organization.models import Building, Floor, Section

#Serializer
from apps.organization.serializers import BuildingSerializer, SectionSerializer, FloorSerializer
class BuildingViewSet(BaseModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    filterset_class = BuildingFilter

    search_fields = ("name","code")
    ordering_fields = ( "name", "code", "created_at")
    ordering = ("name")

class FloorViewSet(BaseModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer
    filterset_class = FloorFilter

    search_fields = ("name","code")
    ordering_fields = ("name", "number")
    ordering = ("name")
    
class SectionViewSet(BaseModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    filterset_class = SectionFilter

    search_fields = ("name", "code")
    ordering_fields = ("name", "code")
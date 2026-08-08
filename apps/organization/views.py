from apps.common.api.mixins import BaseModelViewSet

from apps.organization.filters.building import BuildingFilter
from apps.organization.filters.floor import FloorFilter

from apps.organization.models import Building, Floor

from apps.organization.serializers.building import BuildingSerializer
from apps.organization.serializers.floor import FloorSerializer



class BuildingViewSet(BaseModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    filterset_class = BuildingFilter

    search_fields = ("name","code")
    ordering_fields = ( "name", "code", "created_at")
    ordering = ("name")

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user
            if self.request.user.is_authenticated
            else None
        )

    def perform_update(self, serializer):
        serializer.save(
            updated_by=self.request.user
            if self.request.user.is_authenticated
            else None
        )

class FloorViewSet(BaseModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer
    filterset_class = FloorFilter

    search_fields = ("name","code")
    ordering_fields = ("name", "number")
    ordering = ("name")

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user
            if self.request.user.is_authenticated
            else None
        )

    def perform_update(self, serializer):
        serializer.save(
            updated_by = self.request.user
            if self.request.user.is_authenticated
            else None
        )
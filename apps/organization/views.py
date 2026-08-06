from apps.common.api.mixins import BaseModelViewSet
from apps.organization.filters.building import BuildingFilter
from apps.organization.models import Building
from apps.organization.serializers.building import BuildingSerializer


class BuildingViewSet(BaseModelViewSet):
    queryset = Building.objects.all()

    serializer_class = BuildingSerializer

    filterset_class = BuildingFilter

    search_fields = (
        "name",
        "code",
    )

    ordering_fields = (
        "name",
        "code",
        "created_at",
    )

    ordering = (
        "name",
    )

    def perform_create(self, serializer):
        print(self.request.data)
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
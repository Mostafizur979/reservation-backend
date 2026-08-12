from apps.common.api.mixins import BaseModelViewSet

#Filter
from apps.organization.filters import BuildingFilter, FloorFilter, SectionFilter

#Model
from apps.organization.models import Building, Floor, Section, RoomCategory, Image

#Serializer
from apps.organization.serializers import BuildingSerializer, SectionSerializer, FloorSerializer, ImageSerializer
from apps.organization.models import RoomCategory
from apps.organization.serializers.category import RoomCategorySerializer

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import ValidationError

from apps.common.storage.r2 import (
    upload_to_r2,
    remove_from_r2,
)

class BuildingViewSet(BaseModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    filterset_class = BuildingFilter

    search_fields = ("name","code")
    ordering_fields = ( "name", "code", "created_at")
    ordering = ("name")

    def perform_create(self, serializer):
        serializer.save(
            created_by=(
                self.request.user
                if self.request.user.is_authenticated
                else None
            )
        )

    def perform_update(self, serializer):
        serializer.save(
            updated_by=(
                self.request.user
                if self.request.user.is_authenticated
                else None
            )
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
            created_by=(
                self.request.user
                if self.request.user.is_authenticated
                else None
            )
        )

    def perform_update(self, serializer):
        serializer.save(
            updated_by=(
                self.request.user
                if self.request.user.is_authenticated
                else None
            )
        )
    
class SectionViewSet(BaseModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    filterset_class = SectionFilter

    search_fields = ("name", "code")
    ordering_fields = ("name", "code")

    def perform_create(self, serializer):
        serializer.save(
            created_by=(
                self.request.user
                if self.request.user.is_authenticated
                else None
            )
        )

    def perform_update(self, serializer):
        serializer.save(
            updated_by=(
                self.request.user
                if self.request.user.is_authenticated
                else None
            )
        )

class RoomCategoryViewSet(BaseModelViewSet):
    queryset = RoomCategory.objects.select_related(
        "section",
    ).prefetch_related(
        "images",
    )

    serializer_class = RoomCategorySerializer

    search_fields = (
        "name",
        "bed_type",
        "section__name",
    )

    ordering_fields = (
        "name",
        "base_price",
        "max_adult",
        "max_child",
        "created_at",
        "updated_at",
    )

    ordering = (
        "name",
    )

    def perform_create(self, serializer):
        serializer.save(
            created_by=(
                self.request.user
                if self.request.user.is_authenticated
                else None
            )
        )

    def perform_update(self, serializer):
        serializer.save(
            updated_by=(
                self.request.user
                if self.request.user.is_authenticated
                else None
            )
        )

class ImageViewSet(BaseModelViewSet):

    queryset = Image.objects.select_related(
        "room_category",
    ).all()

    serializer_class = ImageSerializer

    parser_classes = (
        MultiPartParser,
        FormParser,
    )

    search_fields = (
        "room_category__name",
    )

    ordering_fields = (
        "display_order",
        "created_at",
        "updated_at",
    )

    ordering = (
        "display_order",
        "id",
    )

    def perform_create(self, serializer):

        uploaded_file = self.request.FILES.get("image")

        if not uploaded_file:
            raise ValidationError({
                "image": "Image is required."
            })

        image_url = upload_to_r2(
            uploaded_file,
            folder="room-categories",
        )

        serializer.save(
            image=image_url,
            created_by=(
                self.request.user
                if self.request.user.is_authenticated
                else None
            ),
        )

    def perform_update(self, serializer):

        instance = self.get_object()

        old_image = instance.image

        uploaded_file = self.request.FILES.get("image")

        if uploaded_file:

            new_image_url = upload_to_r2(
                uploaded_file,
                folder="room-categories",
            )

            serializer.save(
                image=new_image_url,
                updated_by=(
                    self.request.user
                    if self.request.user.is_authenticated
                    else None
                ),
            )

            # Delete old R2 file
            if old_image:
                remove_from_r2(old_image)

        else:

            serializer.save(
                updated_by=(
                    self.request.user
                    if self.request.user.is_authenticated
                    else None
                )
            )

    def perform_destroy(self, instance):

        if instance.image:
            remove_from_r2(instance.image)

        instance.soft_delete(
            user=(
                self.request.user
                if self.request.user.is_authenticated
                else None
            )
        )
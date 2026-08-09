from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from .responses import ApiResponse


class BaseModelViewSet(ModelViewSet):
    """
    Base ViewSet with standardized responses and soft delete support.
    """

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            created_by=self.request.user
            if self.request.user.is_authenticated
            else None
        )
        return ApiResponse.success(
            data=serializer.data,
            message="Created successfully.",
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            updated_by = self.request.user
            if self.request.user.is_authenticated
            else None
        )
        return ApiResponse.success(
            data=serializer.data,
            message="Updated successfully.",
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.soft_delete(
            user=request.user if request.user.is_authenticated else None
        )
        return ApiResponse.success(message="Deleted successfully.")
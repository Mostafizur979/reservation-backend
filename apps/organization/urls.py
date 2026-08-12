from rest_framework.routers import DefaultRouter

from apps.organization.views import BuildingViewSet, FloorViewSet, SectionViewSet, RoomCategoryViewSet, ImageViewSet

router = DefaultRouter()

router.register("buildings", BuildingViewSet,  basename="building",)
router.register("floors",  FloorViewSet,  basename="floors")
router.register("sections", SectionViewSet, basename="sections")
router.register("category", RoomCategoryViewSet, basename="category")
router.register("images",ImageViewSet, basename="images")

urlpatterns = router.urls
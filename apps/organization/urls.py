from rest_framework.routers import DefaultRouter

from apps.organization.views import BuildingViewSet, FloorViewSet, SectionViewSet

router = DefaultRouter()

router.register("buildings", BuildingViewSet,  basename="building",)
router.register("floors",  FloorViewSet,  basename="floors")
router.register("sections", SectionViewSet, basename="sections")

urlpatterns = router.urls
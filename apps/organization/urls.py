from rest_framework.routers import DefaultRouter

from apps.organization.views import BuildingViewSet, FloorViewSet

router = DefaultRouter()

router.register(
    "buildings",
    BuildingViewSet,
    basename="building",
)

router.register(
    "floors",
    FloorViewSet,
    basename="floors"
)

urlpatterns = router.urls
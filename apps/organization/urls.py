from rest_framework.routers import DefaultRouter

from apps.organization.views import BuildingViewSet

router = DefaultRouter()

router.register(
    "buildings",
    BuildingViewSet,
    basename="building",
)

urlpatterns = router.urls
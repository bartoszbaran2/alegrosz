from rest_framework.routers import DefaultRouter

from . import viewsets

app_name = "products"

router = DefaultRouter()
router.register(r"products", viewsets.ProductViewSet, basename="product-view-set")

urlpatterns = [*router.urls]

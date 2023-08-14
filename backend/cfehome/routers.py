from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSets, ProductGenericViewSet

router = DefaultRouter()
# router.register('product', ProductViewSets, basename="products")
router.register('product', ProductGenericViewSet, basename="products")


print(router.urls)
urlpatterns = router.urls

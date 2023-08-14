from rest_framework import viewsets, mixins
from .models import Product
from .serializers import ProductSerializer


class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"


class ProductGenericViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"


product_list_view = ProductGenericViewSet.as_view({"get": "list"})
produt_detail_view = ProductGenericViewSet.as_view({'get': 'reterive'})

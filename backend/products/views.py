from rest_framework import generics, mixins, permissions, authentication
from rest_framework.response import Response
from api.serializers import ProductSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Product
from api.authentication import TokenAuthentication
from .permissions import IsStaffEditorPermission
from api.mixins import StaffEditorPermissionMixin


class ProductListCreateAPIView(generics.ListCreateAPIView, StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # authentication_classes = [authentication.SessionAuthentication,
    #                           # authentication.TokenAuthentication
    #                           TokenAuthentication
    #                           ]
    # permission_classes = [
    #     permissions.IsAdminUser,
    #     IsStaffEditorPermission,
    # permissions.IsAuthenticated,
    # permissions.DjangoModelPermissions,
    # ]

    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        print(serializer.validated_data)
        serializer.save(content=content)
        # return serializer.save()


class ProductDetaiAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # if you want to overide the queryset
    # def get_queryset(self):
    #     pass


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_delete(self, instance):
        super().perform_destory(instance)


product_detail_view = ProductDetaiAPIView.as_view()
product_list_create_view = ProductListCreateAPIView.as_view()
product_update_view = ProductUpdateAPIView.as_view()
product_delete_view = ProductDestroyAPIView.as_view()


# product_mixin_view = ProductMixinView.as_view()


@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    if request.method == "GET":
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(qs, many=False).data
            return Response(data)
        qs = Product.objects.all()
        data = ProductSerializer(qs, many=True).data
        return Response(data)
    if request.method == "POSt":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # instance= serializer.save()
            # print(instance)
            return Response(serializer.data)
    return Response({"error": "something went wrong"})

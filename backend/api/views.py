from rest_framework.decorators import api_view

from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework import status


# @api_view(["GET"])
# def api_home(request):
#     instance = Product.objects.all().order_by("?").first()
#     if instance:
#         data = ProdcutSerializer(instance).data
#     return Response(data)


@api_view(["POST"])
def api_home(request):
    # data = request.data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance= serializer.save()
        # print(instance)
        return Response(serializer.data)
    return Response({"error": "something went wrong"})

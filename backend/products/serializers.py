from rest_framework import serializers
from products.models import Product
from rest_framework.reverse import reverse


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    # url = serializers.SerializerMethodField(read_only=True)
    #! Only works on a Model Serailizerf
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk"
    )

    class Meta:
        model = Product
        fields = [
            "url",
            "pk",
            "title",
            "price",
            "content",
            "sale_price",
            "my_discount",
        ]

    # def get_url(self, obj):
    #     #!wrong way
    #     # return f"api/products/{obj.id}"

    #     request = self.context.get("request")
    #     if request is None:
    #         return None
    #     return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Product):
            return None
        # try:
        return obj.get_discount()
        # except:
        #     None

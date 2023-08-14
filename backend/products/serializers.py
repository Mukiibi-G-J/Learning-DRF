from rest_framework import serializers
from products.models import Product
from rest_framework.reverse import reverse


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    # url = serializers.SerializerMethodField(read_only=True)
    #! Only works on a Model Serailizer
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk"
    )

    email = serializers.EmailField(write_only=True)

    class Meta:
        model = Product
        fields = [
            "email",
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

    def create(self, validated_data):
        # email = validated_data.pop("email")
        obj = super().create(validated_data)
        # print(email)
        return obj

    def update(self, instance, validated_data):
        print("my instance", instance)
        email = validated_data.pop("email")
        return super().update(instance, validated_data)

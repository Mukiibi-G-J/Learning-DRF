from rest_framework import serializers
from products.models import Product
from rest_framework.reverse import reverse
from .validators import validate_title, validate_title_no_hello, unique_produt_title
from api.serializers import UserPublicSerailizer


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk", read_only=True
    )

    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    # related_products = ProductInlineSerializer(
    #     source="user.product_set.all", read_only=True,
    #     many=True
    # )
    owner = UserPublicSerailizer(source="user", read_only=True)
    # my_discount = serializers.SerializerMethodField(read_only=True)

    # my_user_data = serializers.SerializerMethodField(read_only=True)
    # url = serializers.SerializerMethodField(read_only=True)
    #! Only works on a Model Serailizer
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk"
    )

    email = serializers.EmailField(write_only=True)

    # title = serializers.CharField(validators=[validate_title])
    title = serializers.CharField(
        validators=[validate_title_no_hello, unique_produt_title]
    )
    name = serializers.CharField(source="title", read_only=True)
    #! can also use foregin keys with the source
    # email = serializers.CharField(source="user.email")
    body = serializers.CharField(source="content")

    class Meta:
        model = Product
        fields = [
            # "related_products",
            "owner",
            "email",
            "url",
            "pk",
            "title",
            "price",
            # "content",
            "sale_price",
            # "my_discount",
            # "my_user_data",
            "name",
            "public",
            "body",
            "path"
        ]

    # def get_url(self, obj):
    #     #!wrong way
    #     # return f"api/products/{obj.id}"

    #     request = self.context.get("request")
    #     if request is None:
    #         return None
    #     return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)

    # def get_my_discount(self, obj):
    #     if not hasattr(obj, "id"):
    #         return None
    #     if not isinstance(obj, Product):
    #         return None
    #     # try:
    #     return obj.get_discount()
    #     # except:
    #     #     None

    # def get_my_user_data(self, obj):
    #     return {"username": obj.user.username}

    def create(self, validated_data):
        # email = validated_data.pop("email")
        obj = super().create(validated_data)
        # print(email)
        return obj

    # def validate_title(self, value):
    #     request = self.context.get("request")
    #     user = request.user
    #     qs = Product.objects.filter(user=user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name")
    #     return value

    def update(self, instance, validated_data):
        print("my instance", instance)
        email = validated_data.pop("email")
        return super().update(instance, validated_data)

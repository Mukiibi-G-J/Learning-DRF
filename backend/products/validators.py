from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product


def validate_title(value):
    qs = Product.objects.filter(title__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already a product name")
    return value


def validate_title_no_hello(value):
    #! this can be not allowed email extesions
    if "hello" in value.lower():
        raise serializers.ValidationError(f"hello is not allowed")
    return value


unique_produt_title = UniqueValidator(queryset=Product.objects.all())

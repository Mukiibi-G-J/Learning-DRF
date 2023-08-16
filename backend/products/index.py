from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Product


@register(Product)
class ProductIndex(AlgoliaIndex):
    # should_index = "is_public"
    fields = ["title", "content", "price", "user", "public", "path"]

    settings = {
        "searchableAttributes": ["title", "content"],
        # ! helps ust to narrow down to searhc by public=True or False,  User=Kali
        "attributesForFaceting": ["user", "public"],
    }
    tags = "get_tags_list"

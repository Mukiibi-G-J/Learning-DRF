from django.shortcuts import render
from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.response import Response
from . import client


class SearchListView(generics.GenericAPIView):
    def get(self, *args, **kwargs):
        user = None
        if self.request.user.is_authenticated:
            user = self.request.user.username

        query = self.request.GET.get("q")
        tag = self.request.GET.get("tag") or None
        public = str(self.request.GET.get("public")) != "0"

        if not query:
            return Response("", status=400)
        print(user, query, public, tag)
        results = client.perform_search(query, tags=tag, user=user, public=public)
        return Response(results)


class SearchOldListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get("q")
        results = Product.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user

            results = qs.search(q, user)

        return results

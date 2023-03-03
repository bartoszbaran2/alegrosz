from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers



class ProductViewSet(ModelViewSet):
    queryset = models.Product.objects.all()

    def list(self, request, *args, **kwargs):
        serializer = serializers.ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, pk=None, **kwargs):
        pass

    def create(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, pk=None, **kwargs):
        pass

    def partial_update(self, request, *args, pk=None, **kwargs):
        pass

    def destroy(self, request, *args, pk=None, **kwargs):
        pass
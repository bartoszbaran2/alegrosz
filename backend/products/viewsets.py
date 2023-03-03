from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers



class ProductViewSet(ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, pk=None, **kwargs):
        pass

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def update(self, request, *args, pk=None, **kwargs):
        pass

    def partial_update(self, request, *args, pk=None, **kwargs):
        pass

    def destroy(self, request, *args, pk=None, **kwargs):
        product = get_object_or_404(queryset=self.get_queryset(), pk=pk)
        product.delete()
        return Response(data={}, status=status.HTTP_200_OK)

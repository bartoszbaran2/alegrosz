from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from products.models import Category
from products.paginators import CustomPaginator
from products.serializers import CategorySerializer, CategoryWithSubcategoriesSerializer


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = CustomPaginator
    permission_classes = (IsAuthenticated,)


class CategoryRetrieveView(RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated,)


class CategoryWithSubcategoriesRetrieveView(ListAPIView):
    serializer_class = CategoryWithSubcategoriesSerializer
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated,)

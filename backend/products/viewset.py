from .serializers import ProductSerializer
from rest_framework import viewsets
from .models import Product

class ProductSetView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

from rest_framework import generics, mixins, permissions, authentication
from .models import Product
from products.serializers import ProductSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
# from ..apis.permissions import IsStaffEditorPermission
# from apis.authentication import TokenAuthentication
from apis.mixins import StaffEditorPermissionMixin, UserQuerySetMixin
# view products 
class ProductDetailsAPIView(generics.RetrieveAPIView, UserQuerySetMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_view_details = ProductDetailsAPIView.as_view()

# create products 
class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
     
    # def perform_create(self, serializer):

product_create_view = ProductCreateAPIView.as_view()

# list create products 
class ProductListCreateAPIView(generics.ListCreateAPIView, StaffEditorPermissionMixin, UserQuerySetMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset()
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.one()
    #     return qs.filter(user=request.user)
    # permission_classes = [permissions.IsAuthenticated, IsStaffEditorPermission] => replace with mixin StaffEditorPermissionMixin
    # authentication_classes = [authentication.SessionAuthentication, 
    #                         #   authentication.TokenAuthentication
    #                         TokenAuthentication
    #                           ] => we are setting it in settings.py(cfehome)
     
    # def perform_create(self, serializer):

product_list_create_view = ProductListCreateAPIView.as_view()

# update products

class ProductUpdateAPIView(generics.UpdateAPIView, StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        return super().perform_update(serializer)

product_update_view = ProductUpdateAPIView.as_view()

# destroy product 

class ProductDeleteAPIView(generics.DestroyAPIView, StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

product_delete_view = ProductDeleteAPIView.as_view()

# manual get product, list or create new products

@api_view(['GET', 'POST'])
def product_alt_view(request,pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # get a product
        # get list
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many=True).data
        return Response(data)
      
    if method == "POST":
        # create a product
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "not good way"}, status=400)
    


class ProductMixinView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "this is a single view doing cool stuff"
        serializer.save(content=content)
    
    def patch(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_destroy(self, instance):
        instance.delete()
    
product_mixin_view = ProductMixinView.as_view()

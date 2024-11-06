from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from .validators import validate_title,  unique_product_title
from apis.serializers import UserPublicSerializers
class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializers(source='user', read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-list', lookup_field='pk')
    email = serializers.EmailField(write_only=True)
    title = serializers.CharField(validators=[unique_product_title])
    name = serializers.CharField(source='title')
    class Meta:
        model = Product
        fields = [
            'pk',
            'owner',
            'url',
            'user',
            'email',
            'title',
            'name',
            'content',
            'price',
            'world',
            'sales_price',
            'my_discount',
        ]
    
    # def validate_title(self, value):
    #     # qs = Product.objects.filter(title__exact=value)
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already product")
    #     return value

    # def get_edit_url(self, obj):
    #     request = self.context.get('request') # self.request
    #     if request is None:
    #         return None
    #     return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)
    
    # do not have the field 'email' in database but also we are taking that data 
    def create(self, validated_data):
        email = validated_data.pop('email')
        print(email)
        return super().create(validated_data)
    
    def get_my_discount (self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return  None
        return obj.get_discount()
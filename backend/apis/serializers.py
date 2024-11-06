from rest_framework import serializers

class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-list', lookup_field='pk')
    # email = serializers.EmailField(write_only=True)
    title = serializers.CharField(read_only=True)

class UserPublicSerializers(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    other_products = serializers.SerializerMethodField(read_only=True)

    def get_other_products(self, obj):
        user = obj
        print(user)
        my_products_qs = user.product_set.all()[:5] # context=self.context => request
        return UserProductInlineSerializer(my_products_qs, many=True,context=self.context).data

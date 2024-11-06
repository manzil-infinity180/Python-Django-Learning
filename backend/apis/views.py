from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from products.models import Product

# to work with django rest framework response 
from rest_framework.response import Response
from rest_framework.decorators import api_view

#serializers 
from products.serializers import ProductSerializer

@api_view(['POST']) # Apply which method you gonna used 
def api_home(request, *args, **kwargs):
    print(request.method)
    # instance = Product.objects.all().order_by("?").first()
    # print(instance)
    # data = {}
    # if instance:
    #     # data = model_to_dict(instance)
    #     data = ProductSerializer(instance).data
       
    print(request.data)
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.data)

    # return JsonResponse(data)
        return Response(serializer.data)
    return Response({"invalid": "not good way"}, status=400)
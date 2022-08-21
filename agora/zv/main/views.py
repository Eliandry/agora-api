from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
import json
class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({"products": serializer.data})


class CreateView(APIView):

    def post(self, request):
        data=request.data #type : dict полученные данные от пользователя

       # for i in data:
       #     product=Product()
       #     product.product_id=i['product_id']
       #     product.name=i['name']
       #     product.reference_id=i['reference_id']
        #    product.save()



        return Response('УСПЕШНО')

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
def clean(request):
    pr = Product.objects.all()
    pr.delete()
    return HttpResponseRedirect("/list")

def main(request):
    return render(request,'main.html')
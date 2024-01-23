from django.http import JsonResponse
from django.core import serializers
from .models import Product, Manufacturer
# Create your views here.

# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView


# Simple use with JsonResponse
def product_list(request):
    products = Product.objects.all()  # [:30]
    # data = {"products": list(products.values("pk", "name"))}
    data = {"products": list(products.values())}
    response = JsonResponse(data)
    return response


def product_detail(request, pk: int):
    try:
        product = Product.objects.get(pk=pk)
        data = {
            "product": {
                "name": product.name,
                "manufacturer": product.manufacturer.name,
                "description": product.desciption,
                "photo": product.photo.url,
                "shipping_cost": product.shipping_cost,
                "quantity": product.quantity,
                "price": product.price,
            }
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({
            "error": {
                "code": 404,
                "msg": "product not found!"
            }},
            status=404)


def manufacter_list(request):
    manufacters = Manufacturer.objects.all()
    data = {"manufacters": [*manufacters.values()]}
    response = JsonResponse(data)
    return response


def manufacter_detail(request, pk: int):
    try:
        manufacter = Manufacturer.objects.get(pk=pk)
        data = {
            "manufacter": {
                "id": manufacter.pk,
                "location": manufacter.location,
                "name": manufacter.name
            }
        }
        return JsonResponse(data)
    except Manufacturer.DoesNotExist:
        return JsonResponse({"code": 404, "msg": "manufacter not found!"},
                            status=404)

# Sample use with templates
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "products/product_detail.html"


# class ProductListView(ListView):
#     model = Product
#     template_name = "products/product_list.html"

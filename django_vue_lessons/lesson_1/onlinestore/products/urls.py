from django.urls import path
from .views import product_list, product_detail, manufacter_detail, manufacter_list


urlpatterns = [
    path("products/", product_list, name="product-list"),
    path("products/<int:pk>/", product_detail, name="product-detail"),
    path("manufacters/", manufacter_list, name="manufacter-list"),
    path("manufacters/<int:pk>/", manufacter_detail, name="manufacter-detail")
]


# from .views import ProductDetailView, ProductListView

# urlpatterns = [
#     path("", ProductListView.as_view(), name="product-list"),
#     path("products/<int:pk>", ProductDetailView.as_view(), name="product-detail")
# ]

from django.conf.urls import url

from products.views import (ProductsView, ProductDetailView,
                              CategoryDetailView, CreateProductReviewView, BrandDetailView)

urlpatterns = [
    url(r'^products/$', ProductsView.as_view(), name="products"),
    url(r'^product/(?P<product_slug>[\w-]+)/$', ProductDetailView.as_view(), name="product_detail"),
    url(r'^category/(?P<category_slug>[\w-]+)/$', CategoryDetailView.as_view(), name="category_detail"),
    url(r'^product/(?P<product_slug>[\w-]+)/comment/$', CreateProductReviewView.as_view(), name="comment"),
    url(r'^brand/(?P<brand_id>[\d]+)/$', BrandDetailView.as_view(), name="brand_detail"),

]

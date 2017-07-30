from django.conf.urls import url

from products.views import (ProductsView, ProductDetailView, CategoriesView,
                              CategoryDetailView, CreateProductReviewView)

urlpatterns = [
    url(r'^products/$', ProductsView.as_view(), name="products"),
    url(r'^product/(?P<product_slug>[\w-]+)/$', ProductDetailView.as_view(), name="product_detail"),
    url(r'^$', CategoriesView.as_view(), name="categories_list"),
    url(r'^category/(?P<category_slug>[\w-]+)/$', CategoryDetailView.as_view(), name="category_detail"),
    url(r'^product/(?P<product_slug>[\w-]+)/comment/$', CreateProductReviewView.as_view(), name="comment"),
]

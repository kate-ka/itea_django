from django.db.models.aggregates import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from products.forms import ProductReviewForm
from products.models import Product, Category, ProductReview, Brand


class ProductsView(TemplateView):
    template_name = 'products.html'

    def get_context_data(self, **kwargs):
        context = super(ProductsView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        form = ProductReviewForm()
        context['form'] = form
        context['product_reviews'] = kwargs['object'].get_product_reviews()
        return context


class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    slug_url_kwarg = 'category_slug'
    template_name = 'category_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        category = kwargs['object']
        sort_by = self.request.GET.get("sort_by", "-create_date")
        context['category_products'] = category.sorted_category_products(sort_by)
        return context


class BrandDetailView(DetailView):
    model = Brand
    context_object_name = 'brand'
    template_name = 'brand_detail.html'
    pk_url_kwarg = 'brand_id'

    def get_context_data(self, **kwargs):
        context = super(BrandDetailView, self).get_context_data(**kwargs)
        sort_by = self.request.GET.get("sort_by", "-create_date")
        context['brand_products'] = kwargs['object'].sorted_brand_products(sort_by)
        return context


class CreateProductReviewView(CreateView):
    model = ProductReview
    template_name = 'product_review.html'
    form_class = ProductReviewForm

    def form_valid(self, form):
        product = Product.objects.get(slug=self.kwargs['product_slug'])
        form.instance.product = product
        return super(CreateProductReviewView, self).form_valid(form)

    def get_success_url(self):
        return reverse("product_detail", kwargs={
            "product_slug":self.kwargs['product_slug']
        })


def choose_currency(request):
    user_currency = request.GET.get("currency")
    request.session['currency'] = user_currency
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@receiver(post_save, sender=ProductReview)
def update_product_rating(instance, **kwargs):
    instance.product.rating = instance.product.product_reviews.aggregate(
        average_rating=Avg('rating'))['average_rating']
    instance.product.save()
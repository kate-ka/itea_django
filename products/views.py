from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.signals import request_finished
from django.db.models.aggregates import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from products import apps
from products.forms import ProductReviewForm
from products.models import Product, Category, ProductReview, Brand, AttributeValue


def get_products_page(request, products):
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)
    return products


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
        store_recently_viewed_products(self.request.session, kwargs['object'])
        return context


def store_recently_viewed_products(session, product):
    recently_viewed = session.get('recently_viewed', [])
    if len(recently_viewed) < 3 and product.slug not in recently_viewed:

        recently_viewed.append(product.slug)
    elif len(recently_viewed) >= 3:
        recently_viewed.pop()
        recently_viewed.append(product.slug)
    session['recently_viewed'] = recently_viewed


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
        context['category_attributes'] = category.category_attributes.all()
        attr = self.request.GET.get("sort_by_attr")
        context['attrs'] = attr
        if attr:
            attr_ids = prepare_selected_attribute_ids(attr)
            context['category_products'] = Product.objects.filter(attribute_values__id__in=attr_ids)
        context['category_bestsellers'] = category.get_category_bestsellers()
        context['category_products'] = get_products_page(self.request, context['category_products'])
        context['category_high_rated'] = category.get_category_high_rated_products()
        return context



def prepare_selected_attribute_ids(attr):
    return attr.split(',')


class BrandDetailView(DetailView):
    model = Brand
    context_object_name = 'brand'
    template_name = 'brand_detail.html'
    pk_url_kwarg = 'brand_id'

    def get_context_data(self, **kwargs):
        context = super(BrandDetailView, self).get_context_data(**kwargs)
        sort_by = self.request.GET.get("sort_by", "-create_date")
        brand = kwargs['object']
        context['brand_products'] = get_products_page(self.request, brand.sorted_brand_products(sort_by))
        context['brand_bestsellers'] = brand.get_brand_bestsellers()
        context['brand_high_rated'] = brand.get_brand_high_rated_products()

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
            "product_slug": self.kwargs['product_slug']
        })


def choose_currency(request):
    user_currency = request.GET.get("currency")
    request.session['currency'] = user_currency
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@receiver(post_save, sender=ProductReview)
def update_product_rating(instance, **kwargs):
    instance.product.rating = instance.product.product_reviews.aggregate(
        average_rating=Avg('rating'))['average_rating']
    instance.product.save()
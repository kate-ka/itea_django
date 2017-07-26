from django.db.models.expressions import F
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls.base import reverse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from products.forms import ProductReviewForm
from products.models import Product, Category, ProductReview


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
        return context


class CategoriesView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(CategoriesView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
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


@receiver(post_save, sender=ProductReview)
def update_product_rating(**kwargs):
    review = kwargs['instance']
    product = review.product
    review_rating = review.rating
    if product.rating == 0:
        product.rating = F('rating') + review_rating
    else:
        product.rating = (F('rating') + review_rating) / 2
    product.save()

from django.template.context_processors import request

from products.models import Category


def product_categories(request):
    categories = Category.objects.all()
    return {"product_categories": categories}

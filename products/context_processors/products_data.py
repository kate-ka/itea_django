from django.template.context_processors import request

from products.models import Category, Currency, Product


def products_data(request):
    categories = Category.objects.all()
    currencies = Currency.objects.all()
    default_currency = Currency.objects.filter(is_default=True).first()
    user_currency = Currency.objects.filter(name=request.session.get("currency", default_currency)).first()
    recently_viewed_prod_slugs = request.session.get('recently_viewed', [])
    recently_viewed_products = Product.objects.filter(slug__in=recently_viewed_prod_slugs)
    return {"product_categories": categories,
            "currencies": currencies,
            "default_currency": default_currency,
            "user_currency": user_currency,
            "recently_viewed_products": recently_viewed_products}

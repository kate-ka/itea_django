from django.template.context_processors import request

from products.models import Category, Currency


def product_categories(request):
    categories = Category.objects.all()
    currencies = Currency.objects.all()
    default_currency = Currency.objects.filter(is_default=True).first()
    user_currency = Currency.objects.filter(name=request.session.get("currency")).first()
    return {"product_categories": categories,
            "currencies": currencies,
            "default_currency": default_currency,
            "user_currency": user_currency}

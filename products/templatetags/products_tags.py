from django import template


register = template.Library()


@register.inclusion_tag("templatetags/product_filters.html")
def show_product_filters(instance):
    url_part = instance.get_absolute_url
    return {"url_part": url_part}


@register.simple_tag(takes_context=True)
def show_price_in_user_currency(context, product):
    user_currency = context['user_currency']
    default_currency = context['default_currency']

    if user_currency:

        if default_currency and user_currency != default_currency:
            current_coefficient = user_currency.coefficient/default_currency.coefficient

            return '{} {}'.format(round(product.price * current_coefficient, 2), user_currency.symbol)

    return '{} {}'.format(product.price, product.currency.symbol)



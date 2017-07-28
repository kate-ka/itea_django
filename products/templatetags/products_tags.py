from django import template

register = template.Library()


@register.inclusion_tag("templatetags/product_filters.html")
def show_product_filters(instance):
    url_part = instance.get_absolute_url
    return {"url_part": url_part}


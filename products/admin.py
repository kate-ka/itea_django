from django.contrib import admin
from django.template.defaultfilters import slugify
from django.utils.html import format_html

from .models import (Category, Product, ProductImage, Brand,
                     AttributeName, AttributeValue, ProductReview, Currency)


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]
    prepopulated_fields = {'slug': ['name']}

    list_display = ('name', 'slug', 'brand', 'price', 'quantity', 'is_active', 'product_view')

    filter_horizontal = ['categories', 'attribute_values']

    def save_model(self, request, obj, form, change):
        slug = slugify(obj.name)
        if slug != obj.slug:
            obj.slug = slug

        super(ProductAdmin, self).save_model(request, obj, form, change)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}

    list_display = ('name', 'slug', 'description', 'category_view')
    list_display_links = ('category_view', 'description')

    def save_model(self, request, obj, form, change):
        slug = slugify(obj.name)
        if slug != obj.slug:
            obj.slug = slug
        super(CategoryAdmin, self).save_model(request, obj, form, change)

    def category_view(self, obj):
        return format_html('<img src="%s" width="80px"/>' % obj.image.url)

    category_view.short_description = "Image"


class ProductReviewAdmin(admin.ModelAdmin):
    search_fields = ['product__name']


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'code', 'coefficient')


class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductImage)
admin.site.register(Brand, BrandAdmin)
admin.site.register(AttributeName)
admin.site.register(AttributeValue)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Currency, CurrencyAdmin)

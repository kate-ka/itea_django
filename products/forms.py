from django.forms import ModelForm

from products.models import ProductReview


class ProductReviewForm(ModelForm):
    class Meta:
        model = ProductReview
        fields = ['user', 'text', 'rating']
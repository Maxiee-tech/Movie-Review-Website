from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['movie', 'reviewer_name', 'review_text', 'rating']

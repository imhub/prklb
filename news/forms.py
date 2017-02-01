from django import forms
from .models import Article

class AddNewsForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'blog_content', 'picture',)

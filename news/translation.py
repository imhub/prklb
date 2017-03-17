from modeltranslation.translator import translator, TranslationOptions
from .models import Article

class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'blog_content')
    required_languages = ('en', 'uk', 'de', 'pl')

translator.register(Article, ArticleTranslationOptions)

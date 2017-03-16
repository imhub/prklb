from modeltranslation.translator import translator, TranslationOptions
from .models import Poster

class PosterTranslationOptions(TranslationOptions):
    fields = ('venue', 'show_info')
    required_languages = ('en', 'uk')

translator.register(Poster, PosterTranslationOptions)

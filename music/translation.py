from modeltranslation.translator import translator, TranslationOptions
from .models import Album

class AlbumTranslationOptions(TranslationOptions):
    fields = ('title', 'kind', 'notes')
    required_languages = ('en', 'uk', 'de', 'pl')

translator.register(Album, AlbumTranslationOptions)

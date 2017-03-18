from modeltranslation.translator import translator, TranslationOptions
from .models import Video

class VideoTranslationOptions(TranslationOptions):
    fields = ('title', 'notes')
    required_languages = ('en', 'uk', 'de', 'pl')

translator.register(Video, VideoTranslationOptions)

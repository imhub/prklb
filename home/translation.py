from modeltranslation.translator import translator, TranslationOptions
from .models import HomepageInitialSettings

class HomepageInitialSettingsTranslationOptions(TranslationOptions):
    fields = ('bandsname',)
    required_languages = ('en', 'uk')

translator.register(HomepageInitialSettings, HomepageInitialSettingsTranslationOptions)

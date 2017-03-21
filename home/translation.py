from modeltranslation.translator import translator, TranslationOptions
from .models import HomepageInitialSettings, TechRiderImg, CarouselImg

class HomepageInitialSettingsTranslationOptions(TranslationOptions):
    fields = ('bandsname',)
    required_languages = ('en', 'uk', 'de', 'pl')

class TechRiderImgTranslationOptions(TranslationOptions):
    fields = ('comment',)
    required_languages = ('en', 'uk', 'de', 'pl')

class CarouselImgTranslationOptions(TranslationOptions):
    fields = ('comment',)
    required_languages = ('en', 'uk', 'de', 'pl')

translator.register(HomepageInitialSettings, HomepageInitialSettingsTranslationOptions)
translator.register(TechRiderImg, TechRiderImgTranslationOptions)
translator.register(CarouselImg, CarouselImgTranslationOptions)

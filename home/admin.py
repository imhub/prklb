from django.contrib import admin
from .models import HomepageInitialSettings, LinksBar, TechRiderArch, \
    TechRiderImg, CarouselImg

admin.site.register(HomepageInitialSettings)
admin.site.register(LinksBar)
admin.site.register(TechRiderImg)
admin.site.register(TechRiderArch)
admin.site.register(CarouselImg)

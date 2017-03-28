from django.contrib import admin
from .models import Album, BuyLinks

class BuyLinksInLine(admin.TabularInline):
    model=BuyLinks
    extra = 0

@admin.register(Album)

class AlbumAdmin(admin.ModelAdmin):

    list_display = ("title", '_buylinks')

    search_fields = ["album__title"]

    inlines = [
        BuyLinksInLine
    ]

    def _buylinks(self, obj):
        return obj.buylinks.all().count()

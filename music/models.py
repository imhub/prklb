from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class Album(models.Model):

    class Meta(object):
        verbose_name=_("Album")
        verbose_name_plural=_("Albums")

    title = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        verbose_name=_("Release title")
        )

    kind = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        verbose_name=_("Release type - Album, Single, EP etc.")
        )

    notes = models.TextField(
        blank=False,
        null=False,
        verbose_name=_("Release notes")
        )

    cover = models.ImageField(
        blank=True,
        verbose_name=_("Album cover"),
        null=True
        )

    sc_link = models.CharField(
        max_length = 800,
        blank=True,
        verbose_name=_("Embedded URL to albom at SoundCloud")
        )

    release_date = models.DateField(
        blank=False,
        null=False,
        verbose_name=_("Release Date")
        )

    published_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_("Published, date")
        )

    def publish(self):
        self.save()

    def __str__(self):
        return "%s %s" %(self.title, self.kind)


class BuyLinks(models.Model):

    class Meta(object):
        verbose_name=_("Links to buy or listen to album")
        verbose_name_plural=_("Links to buy or listen to album")

    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name="buylinks",
        verbose_name=_("album")
        )

    linkname = models.CharField(
        max_length = 30,
        blank=True,
        null=True,
        verbose_name=_("Service name")
        )

    linklink = models.URLField(
        max_length = 400,
        blank=True,
        verbose_name=_("Link to album's page on the service")
        )

    linkicon = models.ImageField(
        blank=True,
        verbose_name=_("Service's icon"),
        )

    def __str__(self):
        return "%s" %(self.linkname)

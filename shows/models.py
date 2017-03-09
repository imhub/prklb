from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class Poster(models.Model):

    class Meta(object):
        verbose_name=_("Band shows")
        verbose_name_plural=_("Band shows")

    venue = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        verbose_name=_("City, Venue")
        )

    show_date = models.DateField(
        blank=False,
        null=False,
        verbose_name=_("Date of Show")
        )

    show_info = models.TextField(
        blank=False,
        null=False,
        verbose_name=_("Show Info")
        )

    affiche = models.ImageField(
        blank=True,
        verbose_name=_("Affiche"),
        null=True
        )

    tickets_link = models.URLField(
        max_length = 400,
        blank=True,
        verbose_name=_("Link to buy tickets")
        )

    published_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_("Published, date")
        )

    def publish(self):
        self.save()

    def __str__(self):
        return "%s %s" %(self.venue, self.show_date)

from django.db import models
from django.utils import timezone

class Poster(models.Model):

    class Meta(object):
        verbose_name="Band's shows"
        verbose_name_plural="Band's shows"

    venue = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        verbose_name="City, Venue"
        )

    show_date = models.DateField(
        blank=False,
        null=False,
        verbose_name="Date of Show"
        )

    show_info = models.TextField(
        blank=False,
        null=False,
        verbose_name="Show Info"
        )

    affiche = models.ImageField(
        blank=True,
        verbose_name="Affiche",
        null=True
        )

    tickets_link = models.URLField(
        max_length = 400,
        blank=True,
        verbose_name="Link to buy tickets"
        )

    published_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Опубліковано, дата")

    def publish(self):
        self.save()

    def __str__(self):
        return "%s %s" %(self.venue, self.show_date)

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class Video(models.Model):

    class Meta(object):
        verbose_name=_("Band video")
        verbose_name_plural=_("Band videos")

    title = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        verbose_name=_("Video title")
        )

    notes = models.TextField(
        blank=False,
        null=False,
        verbose_name=_("News text")
        )

    vid = models.CharField(
        max_length = 800,
        blank=True,
        verbose_name=_("Embedded YouTube URL to video")
        )

    created_date = models.DateTimeField(
        default=timezone.now,
        verbose_name=_("Created date")
        )

    published_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_("Published date")
        )

    def publish(self):
        self.published_date = timezone.now(),
        self.save()

    def __str__(self):
        return "%s %s" %(self.title, self.published_date)

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class Article(models.Model):

    class Meta(object):
        verbose_name=_("Band news")
        verbose_name_plural=_("Band news")

    title = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        verbose_name=_("News title")
        )

    blog_content = models.TextField(
        blank=False,
        null=False,
        verbose_name=_("News text")
        )

    picture = models.ImageField(
        blank=True,
        verbose_name=_("Picture"),
        null=True
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

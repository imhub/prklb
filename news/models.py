from django.db import models
from django.utils import timezone

class Article(models.Model):

    class Meta(object):
        verbose_name="Familia Perkalaba news"
        verbose_name_plural="Familia Perkalaba news"

    brief_title = models.CharField(
        blank=False,
        null=False,
        max_length=400,
        verbose_name="Крткй зглвк для головної сторінки"
        )

    title = models.TextField(
        blank=False,
        null=False,
        verbose_name="Заголовок"
        )

    blog_content = models.TextField(
        blank=False,
        null=False,
        verbose_name="Текст новини"
        )

    picture = models.ImageField(
        blank=True,
        verbose_name="Фоточка",
        null=True
        )

    created_date = models.DateTimeField(
        default=timezone.now,
        verbose_name="Написано, дата"
        )

    published_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Опубліковано, дата")

    def publish(self):
        self.published_date = timezone.now(),
        self.save()

    def __str__(self):
        return "%s %s" %(self.title, self.published_date)

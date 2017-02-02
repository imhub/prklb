from django.db import models

class HomepageInitialSettings(models.Model):

    class Meta(object):
        verbose_name="Band's settings"
        verbose_name_plural="Band's settings"

    bandsname = models.TextField(
        blank=False,
        null=False,
        verbose_name="Band's Name"
        )

    logo = models.ImageField(
        blank=True,
        verbose_name="Band's Logo",
        null=True
        )

    rider = models.ImageField(
        blank=True,
        verbose_name="Technical Rider",
        null=True
        )

    phone = models.CharField(
        max_length = 15,
        blank=False,
        null=False,
        verbose_name="Management Phone"
        )

    email = models.CharField(
        max_length = 30,
        blank=False,
        null=False,
        verbose_name="Management Email"
        )

    skype = models.CharField(
        max_length = 30,
        blank=False,
        null=False,
        verbose_name="Management Skype"
        )

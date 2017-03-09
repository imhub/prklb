from django.db import models
from django.utils.translation import ugettext_lazy as _

class HomepageInitialSettings(models.Model):

    class Meta(object):
        verbose_name=_("Site's initial settings")
        verbose_name_plural=_("Site's initial settings")

    bandsname = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        verbose_name=_("Band Name")
        )

    logo = models.ImageField(
        blank=True,
        verbose_name=_("Band Logo"),
        null=True
        )

    rider = models.ImageField(
        blank=True,
        verbose_name=_("Technical Rider"),
        null=True
        )

    phone = models.CharField(
        max_length = 15,
        blank=False,
        null=False,
        verbose_name=_("Management Phone")
        )

    email = models.EmailField(
        max_length = 254,
        blank=False,
        null=False,
        verbose_name=_("Management Email")
        )

    skype = models.CharField(
        max_length = 30,
        blank=False,
        null=False,
        verbose_name=_("Management Skype")
        )

    homepage_pic_top = models.ImageField(
        blank=True,
        verbose_name=_("Homepage Top Pictire"),
        null=True
        )

    homepage_pic_bottom = models.ImageField(
        blank=True,
        verbose_name=_("Homepage Bottom Pictire"),
        null=True
        )

    newspage_pic = models.ImageField(
        blank=True,
        verbose_name=_("Newspage Pictire"),
        null=True
        )

    showspage_pic = models.ImageField(
        blank=True,
        verbose_name=_("Showspage Pictire"),
        null=True
        )

    albumspage_pic = models.ImageField(
        blank=True,
        verbose_name="Albumspage Pictire",
        null=True
        )

    musicpage_pic = models.ImageField(
        blank=True,
        verbose_name=_("Musicpage Pictire"),
        null=True
        )

class LinksBar(models.Model):

    class Meta(object):
        verbose_name=_("Band's links, social buttons etc")
        verbose_name_plural=_("Band's links, social buttons etc")

    linkname = models.CharField(
        max_length = 30,
        blank=False,
        null=False,
        verbose_name=_("Service name")
        )

    linklink = models.URLField(
        max_length = 400,
        blank=True,
        verbose_name=_("Link to band's page on the service")
        )

    linkicon = models.ImageField(
        blank=False,
        verbose_name=_("Service's icon"),
        )

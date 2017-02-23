from django.db import models

class HomepageInitialSettings(models.Model):

    class Meta(object):
        verbose_name="Site's initial settings"
        verbose_name_plural="Site's initial settings"

    bandsname = models.CharField(
        max_length=200,
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

    email = models.EmailField(
        max_length = 254,
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

    homepage_pic_top = models.ImageField(
        blank=True,
        verbose_name="Homepage Top Pictire",
        null=True
        )

    homepage_pic_bottom = models.ImageField(
        blank=True,
        verbose_name="Homepage Bottom Pictire",
        null=True
        )

    newspage_pic = models.ImageField(
        blank=True,
        verbose_name="Newspage Pictire",
        null=True
        )

    showspage_pic = models.ImageField(
        blank=True,
        verbose_name="Showspage Pictire",
        null=True
        )

    albumspage_pic = models.ImageField(
        blank=True,
        verbose_name="Albumspage Pictire",
        null=True
        )

    musicpage_pic = models.ImageField(
        blank=True,
        verbose_name="Musicpage Pictire",
        null=True
        )

class LinksBar(models.Model):

    class Meta(object):
        verbose_name="Band's links, social buttons etc"
        verbose_name_plural="Band's links, social buttons etc"

    linkname = models.CharField(
        max_length = 30,
        blank=False,
        null=False,
        verbose_name="Service name"
        )

    linklink = models.URLField(
        max_length = 400,
        blank=True,
        verbose_name="Link to band's page on the service"
        )

    linkicon = models.ImageField(
        blank=False,
        verbose_name="Service's icon",
        )

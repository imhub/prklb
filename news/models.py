from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=400)
    blog_content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

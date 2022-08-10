from django.db import models
from django.utils.text import slugify

class Notifications(models.Model):
    text = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Notifications, self).save(*args, **kwargs)


def notification_post_save(*args, **kwargs):
    print("post_save")
    print(args, kwargs)

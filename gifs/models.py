import os
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

def upload_to(instance, filename):
    path = os.path.join(instance.user.username, '-'.join(['%Y%m%d', '%H%M%S', filename]))
    now = datetime.now()

    return now.strftime(path)

class GifManager(models.Manager):
    use_for_related_fields = True

    def latest_gif(self):
        qs = super(GifManager, self).get_query_set()

        try:
            return qs.order_by('-created').all()[0]
        except IndexError:
            return None

class Gif(models.Model):
    user = models.ForeignKey(User, related_name='gifs')
    image = models.ImageField(upload_to=upload_to)
    objects = GifManager()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True, auto_now=True)

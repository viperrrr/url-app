from django.db import models
from django.contrib.auth.models import User

from I4G003785C5D.links.managers import ActiveLinkManager

# Create your models here.

class Links(models.Model):
    target_URL = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=200, blank=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField()
    objects = models.Manager()
    public = ActiveLinkManager()

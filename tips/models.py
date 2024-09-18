from django.db import models


# Create your models here.

class Tip(models.Model):
    content: models.TextField()
    date: models.DateTimeField()
    user: models.CharField()

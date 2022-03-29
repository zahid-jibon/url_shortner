from django.db import models


# Create your models here.
class Url(models.Model):
    link = models.CharField(max_length=10000, null=True)
    uuid = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.link

 
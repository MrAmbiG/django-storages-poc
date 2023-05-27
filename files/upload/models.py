from django.db import models


class FileModel(models.Model):
    name = models.CharField(max_length=60,null=True, blank=True)
    description = models.TextField()
    userfile = models.FileField(null=True, blank=True)


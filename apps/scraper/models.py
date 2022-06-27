from django.db import models

# Create your models here.


class Url(models.Model):
    url = models.URLField()


class Keyword(models.Model):
    keyword = models.CharField(max_length=50)
    url = models.ForeignKey(Url,on_delete=models.CASCADE)

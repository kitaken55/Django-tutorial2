from django.db import models

# Create your models here.

class BoardModel(models.Model):
    title = models.CharField(max_length=100) 
    content = models.TextField()
    author = models.CharField(max_length=200)
    images = models.ImageField(upload_to='') # ''(ブランク)にすることで、setting.pyで設定した値になる。
    good = models.IntegerField(null=True, blank=True, default=0)
    read = models.IntegerField(null=True, blank=True, default=0)
    readtext = models.CharField(max_length=100, null=True, blank=True, default="a")
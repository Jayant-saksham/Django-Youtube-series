from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    thumnail = models.ImageField(null = True, blank = True, default = "Hello.png")
    user = models.ForeignKey(User, default=None,  on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def getBodySlice(self):
        return self.body[:40] + "..."



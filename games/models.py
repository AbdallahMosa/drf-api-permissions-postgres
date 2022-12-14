from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=255)
    purchaser= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description =models.TextField(default="description")
    img_url=models.TextField(default='please add image url')
    def __str__(self) :
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description =models.TextField(default="description")
    purchaser= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    def __str__(self) :
        return self.title
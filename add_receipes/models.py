from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Receipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True , blank = True)
    receipe_name = models.CharField("Name", max_length=20)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to ='images')
    receipe_view_count = models.IntegerField(default = 1)

    def __str__(self) -> str:
        return self.receipe_name


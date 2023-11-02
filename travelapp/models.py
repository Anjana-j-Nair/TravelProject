from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')
    des=models.TextField()
    def __str__(self):
        return self.name
class Team(models.Model):
    name=models.CharField(max_length=200)
    pic=models.ImageField(upload_to='pics')
    d=models.TextField()
    def __str__(self):
        return self.name
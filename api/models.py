from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cantidad = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return '$s $s $s $s' % (self.title, self.description, self.cantidad, self.time)

class User(models.Model):
    nombre = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    
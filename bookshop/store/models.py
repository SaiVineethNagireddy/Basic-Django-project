from django.db import models
#the model
#creating models for our database
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=225)
    price = models.IntegerField()
    stock = models.IntegerField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
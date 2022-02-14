from django.db import models

class TodoListItem(models.Model):
    content = models.TextField()  


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField() 
    size = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



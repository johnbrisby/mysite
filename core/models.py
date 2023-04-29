from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Doctype(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category,related_name='item',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField(blank=True,null=True)
    image = models.ImageField(upload_to='item_images',blank=True,null=True)
    created_by = models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    doc_type = models.ForeignKey(Doctype,related_name='item',on_delete=models.CASCADE)
    doc_link = models.TextField(max_length=255,blank=True,null=True)
    total_views=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name

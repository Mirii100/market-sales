from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)
    



    class Meta:
        ordering=('name',)
        verbose_name_plural='Categories'

    def __str__(self):
        return f'name is {self.name}'
    

class Item(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    price=models.FloatField(default='10')
    is_sold=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
    category=models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    # for adding image 
    image=models.ImageField(upload_to='item_images',blank=True,null=True)

    def __str__(self):
        return (f'{self.name} {self.description} {self.price} {self.created_by} {self.created_at}')

from django.db import models

class Truck(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    coolStuff = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
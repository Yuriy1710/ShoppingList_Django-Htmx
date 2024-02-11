from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
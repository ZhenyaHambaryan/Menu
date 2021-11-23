from django.db import models

class Slide(models.Model):
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)

# Create your models here.

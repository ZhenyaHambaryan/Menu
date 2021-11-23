from django.db import models

class Slide(models.Model):
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    alt = models.CharField(null=True, max_length=255, blank=True)

# Create your models here.

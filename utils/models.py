from django.db import models


class Images(models.Model):
  image = models.ImageField(upload_to='uploads/', null=True, blank=True)


class Slide(models.Model):
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    alt = models.CharField(null=True, max_length=255, blank=True)


class ContactUs(models.Model):
  name = models.CharField(null=True,blank=True,max_length=255)
  phone_number = models.CharField(null=True,blank=True,max_length=255)
  email = models.CharField(null=True,blank=True,max_length=255)
  subject =  models.CharField(null=True,blank=True,max_length=1000)
  message =  models.CharField(null=True,blank=True,max_length=1000)

class TimeInterval(models.Model):
  start_time = models.TimeField(auto_now=False, auto_now_add=False)
  end_time =models.TimeField(auto_now=False, auto_now_add=False)


# Create your models here.

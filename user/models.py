from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, PROTECT, SET_NULL


class UserDetail(models.Model):
  # Django default User model contains:
    # username      # user_permissions
    # first_name    # is_staff
    # last_name     # is_active
    # email         # is_superuser
    # password      # last_login
    # groups        # date_joined
 
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_details", primary_key = True)
  phone_number = models.CharField(null=True,blank=True,max_length=255)
  birth_date = models.DateField(null=True, blank=True)
  about = models.CharField(null=True,blank=True,max_length=1000)
  zip_code = models.CharField(null=True,blank=True,max_length=255)
  city = models.CharField(null=True,blank=True, max_length=255)
  city_longitude = models.CharField(null=True,blank=True,max_length=255)
  city_latitude = models.CharField(null=True,blank=True,max_length=255)
  address = models.CharField(null=True,blank=True,max_length=1000)
  address_longitude = models.CharField(null=True,blank=True,max_length=255)
  address_latitude = models.CharField(null=True,blank=True,max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  organizations = models.ManyToManyField('user.Organization', blank=True)
  is_client = models.BooleanField(default=True)
  is_master = models.BooleanField(default=False)
  fave_foods = models.ManyToManyField('food.Food', blank=True)

  def __str__(self):
    return self.user.get_full_name()

class Organization(models.Model):
  name = models.CharField(null=True,blank=True,max_length=255)
  org_leader = models.ForeignKey(User,null=True,blank=True,on_delete=SET_NULL)
  phone_number = models.CharField(null=True,blank=True,max_length=255)
  about = models.CharField(null=True,blank=True,max_length=1000)
  zip_code = models.CharField(null=True,blank=True,max_length=255)
  city = models.CharField(null=True,blank=True, max_length=255)
  city_longitude = models.CharField(null=True,blank=True,max_length=255)
  city_latitude = models.CharField(null=True,blank=True,max_length=255)
  address = models.CharField(null=True,blank=True,max_length=1000)
  address_longitude = models.CharField(null=True,blank=True,max_length=255)
  address_latitude = models.CharField(null=True,blank=True,max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.name

class ContactUs(models.Model):
  name = models.CharField(null=True,blank=True,max_length=255)
  phone_number = models.CharField(null=True,blank=True,max_length=255)
  email = models.CharField(null=True,blank=True,max_length=255)
  subject =  models.CharField(null=True,blank=True,max_length=1000)
  message =  models.CharField(null=True,blank=True,max_length=1000)


class ConfirmCode(models.Model):
  code = models.CharField(max_length=255, blank=False, null=False, primary_key=True)
  phone_number = models.CharField(null=True,blank=True,max_length=255)
  email = models.CharField(null=True,blank=True,max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.code


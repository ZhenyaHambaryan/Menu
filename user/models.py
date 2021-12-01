from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, PROTECT, SET_NULL

TEAM_STATUS=[
  ("pending", 'в ожидании'),
  ("accepted",'принято'),
  ("canceled",'отменено'),
  ("rejected",'отклоненный')
]

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
  # organizations = models.ManyToManyField('user.Organization', blank=True)
  is_client = models.BooleanField(default=True)
  is_master = models.BooleanField(default=False)
  # fave_foods = models.ManyToManyField('food.Food', blank=True)

  def __str__(self):
    return self.user.get_full_name()

#
# class City(models.Model):
#   city = models.CharField(null=True,blank=True, max_length=255)
#   city_longitude = models.CharField(null=True,blank=True,max_length=255)
#   city_latitude = models.CharField(null=True,blank=True,max_length=255)


class Team(models.Model):
  name = models.CharField(null=True,blank=True,max_length=255)
  team_leader = models.ForeignKey(User,null=True,blank=True,on_delete=CASCADE,related_name="team_user")
  phone_number = models.CharField(null=True,blank=True,max_length=255)
  about = models.CharField(null=True,blank=True,max_length=1000)
  zip_code = models.CharField(null=True,blank=True,max_length=255)
  address = models.CharField(null=True,blank=True,max_length=1000)
  address_longitude = models.CharField(null=True,blank=True,max_length=255)
  address_latitude = models.CharField(null=True,blank=True,max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  # city = models.ForeignKey(City,null=True,blank=True,on_delete=CASCADE,related_name="team_city")

  def __str__(self):
    return self.name

class RequestTeam(models.Model):
  user = models.ForeignKey(User,null=True,blank=True,on_delete=CASCADE,related_name="user_request")
  team = models.ForeignKey(Team,null=True,blank=True,on_delete=CASCADE,related_name="team_request")
  status = models.CharField(max_length=255, null=True, blank=True,default='pending',  choices=TEAM_STATUS)




class UserTeam(models.Model):
  user = models.ForeignKey(User,null=True,blank=True,on_delete=CASCADE,related_name="user_team")
  team = models.ForeignKey(Team,null=True,blank=True,on_delete=CASCADE,related_name="team_user")
  # user_status = models.CharField(max_length=255, null=True, blank=True, choices=TEAM_STATUS)



class ConfirmCode(models.Model):
  code = models.CharField(max_length=255, blank=False, null=False, primary_key=True)
  # phone_number = models.CharField(null=True,blank=True,max_length=255)
  email = models.CharField(null=True,blank=True,max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.code

class RecoverEmail(models.Model):
  token = models.CharField(max_length=255, blank=False, null=False, primary_key=True)
  email = models.CharField(null=True,blank=True,max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)


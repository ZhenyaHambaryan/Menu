from django.db.models import fields
from user.models import UserDetail,ContactUs,Team
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id','username','first_name','last_name','email','is_active',
     'last_login', 'date_joined')

class UserDetailSerializer(serializers.ModelSerializer):
  user=UserSerializer()
  def to_representation(self, instance):
    representation = super(UserDetailSerializer,self).to_representation(instance)
    representation["id"] = instance.user.id
    return representation
  class Meta:
    model = UserDetail
    fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
  class Meta:
    model = Team
    fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
  class Meta:
    model = ContactUs
    fields = '__all__'

#
# class CitySerializer(serializers.ModelSerializer):
#   class Meta:
#     model = City
#     fields = '__all__'
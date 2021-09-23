from django.db.models import fields
from user.models import Organization, UserDetail
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('username','first_name','last_name','email','is_active',
     'last_login', 'date_joined')

class UserDetailSerializer(serializers.ModelSerializer):
  user=UserSerializer()
  # def to_representation(self, instance):
  #   representation = super(UserDetailSerializer,self).to_representation(instance)
  #   representation["user"] = UserSerializer(instance.user).data
  #   return representation
  class Meta:
    model = UserDetail
    fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Organization
    fields = '__all__'
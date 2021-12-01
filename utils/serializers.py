from django.db.models import fields
from utils.models import Slide,ContactUs
from rest_framework import serializers

class SlideSerializer(serializers.ModelSerializer):
  class Meta:
    model = Slide
    fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
  class Meta:
    model = ContactUs
    fields = '__all__'
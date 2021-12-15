from django.db.models import fields
from utils.models import Slide,ContactUs,TimeInterval,Images
from rest_framework import serializers


class ImagesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Images
    fields = '__all__'


class SlideSerializer(serializers.ModelSerializer):
  class Meta:
    model = Slide
    fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
  class Meta:
    model = ContactUs
    fields = '__all__'

class TimeIntervalSerializer(serializers.ModelSerializer):
  class Meta:
    model = TimeInterval
    fields = '__all__'
from django.db.models import fields
from utils.models import Slide
from rest_framework import serializers

class SlideSerializer(serializers.ModelSerializer):
  class Meta:
    model = Slide
    fields = '__all__'

from django.shortcuts import render
from rest_framework import viewsets
from .models import  Slide
from .serializers import SlideSerializer


class SlideViewSet(viewsets.ModelViewSet):
  queryset = Slide.objects.all()
  serializer_class = SlideSerializer


# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets
from .models import  Slide,ContactUs, TimeInterval,Images
from .serializers import SlideSerializer,ContactUsSerializer,TimeIntervalSerializer,ImagesSerializer



class ImagesViewSet(viewsets.ModelViewSet):
  queryset = Images.objects.all()
  serializer_class = ImagesSerializer


class SlideViewSet(viewsets.ModelViewSet):
  queryset = Slide.objects.all()
  serializer_class = SlideSerializer


class ContactUsViewSet(viewsets.ModelViewSet):
  queryset = ContactUs.objects.all()
  serializer_class = ContactUsSerializer

class TimeIntervalViewSet(viewsets.ModelViewSet):
  queryset = TimeInterval.objects.all()
  serializer_class = TimeIntervalSerializer

# Create your views here.

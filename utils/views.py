from django.shortcuts import render
from rest_framework import viewsets
from .models import  Slide,ContactUs
from .serializers import SlideSerializer,ContactUsSerializer


class SlideViewSet(viewsets.ModelViewSet):
  queryset = Slide.objects.all()
  serializer_class = SlideSerializer


class ContactUsViewSet(viewsets.ModelViewSet):
  queryset = ContactUs.objects.all()
  serializer_class = ContactUsSerializer
# Create your views here.

from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import SlideViewSet,ContactUsViewSet
from utils import views

slide_list = SlideViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

slide_detail = SlideViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

contact_us_list = ContactUsViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

contact_us_detail = ContactUsViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [

    path('slide/', slide_list, name='slide-list'),
    path('slide/<int:pk>/', slide_detail, name='slide-detail'),
    path('contact_us/', contact_us_list, name='contact-us-list-list'),
    path('contact_us/<int:pk>/', contact_us_detail, name='contact-us-detail'),
]
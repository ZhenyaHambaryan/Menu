from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import SlideViewSet,ContactUsViewSet,TimeIntervalViewSet,ImagesViewSet
from utils import views

images_list = ImagesViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

images_detail = ImagesViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

time_interval_list = TimeIntervalViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

time_interval_detail = TimeIntervalViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

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
    path('time_interval/', time_interval_list, name='time-interval-list'),
    path('time_interval/<int:pk>/', time_interval_detail, name='time-interval-detail'),
    path('images/', images_list, name='images-list'),
    path('images/<int:pk>/', images_detail, name='images-detail'),
]
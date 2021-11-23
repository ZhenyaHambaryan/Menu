from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import SlideViewSet
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


urlpatterns = [

    path('slide/', slide_list, name='slide-list'),
    path('slide/<int:pk>/', slide_detail, name='slide-detail'),

]
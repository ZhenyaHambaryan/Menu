
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from django.urls import path

from files import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'', views.FileViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
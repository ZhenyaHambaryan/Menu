from django.shortcuts import render
from files.models import File
from files.serializers import FileSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from files.models import File


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def create(self, request):
        file = super().create(request)
        file_url = file.data['file_url'].replace("/files/files", "").replace("127.0.0.1:8000", "192.168.1.107:8000")
        File.objects.get(id=file.data['id']).delete()
        return Response({"url": file_url})

# Create your views here.

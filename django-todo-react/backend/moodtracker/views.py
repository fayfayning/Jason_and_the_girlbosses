from django.shortcuts import render
from rest_framework import viewsets
from .serializers import moodUpdateSerializer
from .models import moodUpdate

# Create your views here.

class moodUpdateView(viewsets.ModelViewSet):
    serializer_class = moodUpdateSerializer
    queryset = moodUpdate.objects.all()

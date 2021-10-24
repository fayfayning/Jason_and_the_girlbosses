from django.shortcuts import render
from rest_framework import viewsets
from .serializers import moodUpdateSerializer
from .models import moodUpdate
from .forms import moodUpdateForm

# Create your views here.

class moodUpdateView(viewsets.ModelViewSet):
    serializer_class = moodUpdateSerializer
    queryset = moodUpdate.objects.all()

    def upload(request):
        form = moodUpdateForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.uploaded_by = request.user
            instance.save()
            form.save_m2m()
from rest_framework import serializers
from .models import moodUpdate

class moodUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = moodUpdate
        fields = ('mood', 'journal_entry') # Whatever we end up adding to the moodtracker model
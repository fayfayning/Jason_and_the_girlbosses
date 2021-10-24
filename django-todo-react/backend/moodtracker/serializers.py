from rest_framework import serializers
from .models import moodUpdate

class moodUpdateSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = moodUpdate
        fields = ('uploaded_by','mood', 'journal_entry') # Whatever we end up adding to the moodtracker model
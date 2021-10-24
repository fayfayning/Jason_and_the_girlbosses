from django import forms
from .models import moodUpdate

class moodUpdateForm(forms.ModelForm):

    """"
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(moodUpdateForm, self).__init__(*args, **kwargs)
    """

    HAPPY = 'H'
    SAD = 'S'
    ANGRY = 'A'
    ANXIOUS = 'X'
    STRESSED = 'T'
    CONFIDENT = 'C'
    OVERWHELMED = 'O'
    FINE = 'F'
    MOOD_CHOICES = [
        (HAPPY, "Happy"),
        (SAD, 'Sad'),
        (ANGRY, 'Angry'),
        (ANXIOUS, 'Anxious'),
        (STRESSED, 'Stressed'),
        (CONFIDENT, "Confident"),
        (OVERWHELMED, "Overwhelmed"),
        (FINE, 'Fine')
    ]
    mood = forms.ChoiceField(
        #max_length = 1,
        choices = MOOD_CHOICES,
        #default = FINE
    )
    message = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = moodUpdate
        fields = ['uploaded_by', 'mood', 'journal_entry']
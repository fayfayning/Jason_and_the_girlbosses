from django.db import models

# Create your models here

# Theoretically everything that's currently in personal_data.py should be
# in here and in Django model form

class moodUpdate(models.Model):
    uploaded_by = models.ForeignKey('auth.User',default=1,related_name='uploads',on_delete=models.CASCADE,)
    #current_user = models.CharField(max_length=150)
    """"
    def get_object(self):
        return self.request.user
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
    mood = models.CharField(max_length = 1, choices = MOOD_CHOICES)
    journal_entry = models.CharField(max_length=1000)

    def is_doing_well(self):
        return self.mood in {self.HAPPY, self.CONFIDENT}
    
    def is_doing_fine(self):
        return self.mood in {self.FINE}
    
    def is_struggling(self):
        return self.mood in {self.ANXIOUS, self.OVERWHELMED}
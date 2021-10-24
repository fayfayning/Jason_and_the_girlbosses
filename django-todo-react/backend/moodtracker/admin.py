from django.contrib import admin
from .models import moodUpdate
# Whatever model classes we make

# Register your models here.

""" 
Syntax for this should show all of the model classes that we make
kinda like this for each:
"""

class moodUpdateAdmin(admin.ModelAdmin):
    list_display = ('uploaded_by', 'mood', 'journal_entry')

admin.site.register(moodUpdate, moodUpdateAdmin)
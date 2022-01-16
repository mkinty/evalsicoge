from django.contrib import admin
from .models import Quiz


# Register your models here.

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('stage', 'stage_name', 'place', 'teacher', 'organization1',
                    'organization2', 'organization3', 'other_formation1', 'other_formation2',
                    'other_formation_type1', 'other_formation_type2', 'find')

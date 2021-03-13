from django.contrib import admin
from .models import Questions

# Register your models here.


class QuestionsAdmin(admin.ModelAdmin):
    list_display = (
        'question_number',
        'date',
        'name',
        'email',
        'question',
    )


admin.site.register(Questions, QuestionsAdmin)
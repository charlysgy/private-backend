from django.contrib import admin

from .models import *

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Theme', {'fields': ['theme']}),
        ('Question', {'fields': ['question_text']}),
        ('Choice', {'fields': ['choice_text']}),
    ]
    list_filter = ['theme']
    search_fields = ['choice_text']

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 10

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Theme', {'fields': ['theme']}),
        ('Question', {'fields': ['question_text']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['theme']
    search_fields = ['question_text']

class ThemeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Theme', {'fields': ['theme_text']}),
    ]
    search_fields = ['theme_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Theme, ThemeAdmin)
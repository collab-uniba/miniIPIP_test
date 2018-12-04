from django.contrib import admin
from .models import Question,Choice,People

class Peoples(admin.TabularInline):
    model = People
    extra = 0


class ChoiceinLine(admin.TabularInline):
    model = Choice
    extra = 0

class OnePeople(admin.ModelAdmin):
    list_display = ('id_test','extraversion','agreeableness','neuroticism','coscientiousness','openness')


admin.site.register(People,OnePeople)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text','cat')
    fieldsets = [
            (None,{'fields': ['question_text','score']}),
            ('Categoria', {'fields': ['cat']})
                ]
    inlines = [ChoiceinLine]

admin.site.register(Question, QuestionAdmin)
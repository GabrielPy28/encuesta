from django.contrib import admin
import nested_admin
from .models import Quiz, QuizTaker, Questions, Answer, UsersAnswer

class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 4
    max_num = 4

class QuestionsInline(nested_admin.NestedTabularInline):
    model = Questions
    inliens = [AnswerInline,]
    extra = 5

class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionsInline,]

class UsersAsnswerInline(admin.TabularInline):
    model = UsersAnswer

class QuizTakerAdmin(admin.ModelAdmin):
    inlines = [UsersAsnswerInline, ]

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Questions)
admin.site.register(QuizTaker, QuizTakerAdmin)
admin.site.register(Answer)
admin.site.register(UsersAnswer)

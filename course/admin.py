from django.contrib import admin
# Seven imported classes (Course, Lesson, Enrollment, Question, Choice, Submission + admin)
from .models import Course, Lesson, Enrollment, Question, Choice, Submission

# --- TASK 2: Implementation of Inlines and Admins ---

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 5

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class LessonAdmin(admin.ModelAdmin):
    # This allows you to add Questions directly when editing a Lesson
    inlines = [QuestionInline]

# Registering the models to the Admin site
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Enrollment)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
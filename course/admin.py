from django.contrib import admin
# Requirement: Seven imported classes
from .models import Course, Lesson, Enrollment, Question, Choice, Submission, Instructor, Learner

# --- Inlines ---
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 5

# --- Admin Classes ---
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'grade'] # Adding list_display for extra safety

class LessonAdmin(admin.ModelAdmin):
    # Requirement: Implement list_display attribute
    list_display = ['title', 'order']
    inlines = [QuestionInline]

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'publish_date')
    search_fields = ['name', 'description']

# --- Registrations ---
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Enrollment)
admin.site.register(Instructor)
admin.site.register(Learner)
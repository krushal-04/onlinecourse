from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson, Question, Choice, Submission, Enrollment

# --- TASK 5: submit and show_exam_result functions ---

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        # Get selected choices from the checkbox inputs in the template
        selected_ids = request.POST.getlist('choice')
        
        if selected_ids:
            # For the purpose of this project, we assume the first enrollment 
            # or create a dummy one if it doesn't exist to link the submission
            enrollment = Enrollment.objects.filter(course=course).first()
            
            # Create a new submission object
            submission = Submission.objects.create(enrollment=enrollment)
            
            # Add the selected choices to the submission
            for choice_id in selected_ids:
                choice = get_object_or_404(Choice, pk=choice_id)
                submission.choices.add(choice)
            
            # Redirect to the result view
            return redirect('course:show_exam_result', submission.id)
            
    return redirect('course:course_details', course_id=course.id)

def show_exam_result(request, submission_id):
    # Retrieve the specific submission
    submission = get_object_or_404(Submission, pk=submission_id)
    course = submission.enrollment.course
    
    # Calculate the score
    total_questions = Question.objects.filter(lesson__course=course).count()
    # Count how many of the submitted choices are marked as 'is_correct=True'
    correct_choices_count = submission.choices.filter(is_correct=True).count()
    
    context = {
        'submission': submission,
        'course': course,
        'total': total_questions,
        'correct': correct_choices_count,
    }
    
    return render(request, 'course/exam_result.html', context)
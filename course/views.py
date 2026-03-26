from django.shortcuts import render, redirect
from .models import Submission

def submit(request, course_id):
    if request.method == 'POST':
        selected = request.POST.getlist('choice')

        submission = Submission.objects.create(enrollment_id=1)
        submission.choices.set(selected)

        return redirect('show_exam_result', submission.id)

def show_exam_result(request, submission_id):
    submission = Submission.objects.get(id=submission_id)

    total = submission.choices.count()
    correct = submission.choices.filter(is_correct=True).count()

    return render(request, 'exam_result.html', {
        'total': total,
        'correct': correct
    })
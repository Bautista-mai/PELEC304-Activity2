from django.shortcuts import render, get_object_or_404
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student.objects.select_related('background'), pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})
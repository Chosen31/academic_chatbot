from .models import Student, Course, Progress

def get_student_info(student_id):
    try:
        student = Student.objects.get(student_id=student_id)
        return f"Student: {student.first_name} {student.last_name}, GPA: {student.gpa}"
    except Student.DoesNotExist:
        return "Student not found."

def get_course_info(course_name):
    try:
        course = Course.objects.get(name=course_name)
        return f"Course: {course.name}, Credits: {course.credits}, Description: {course.description}"
    except Course.DoesNotExist:
        return "Course not found."

def get_progress(student_id, course_name):
    try:
        student = Student.objects.get(student_id=student_id)
        course = Course.objects.get(name=course_name)
        progress = Progress.objects.get(student=student, course=course)
        return f"Progress for {student.first_name} in {course.name}: {progress.grade}"
    except (Student.DoesNotExist, Course.DoesNotExist, Progress.DoesNotExist):
        return "Progress not found."

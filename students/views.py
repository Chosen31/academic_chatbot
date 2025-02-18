from rest_framework import viewsets
from .models import Student, Course, Progress
from .serializers import StudentSerializer, CourseSerializer, ProgressSerializer
from .chatbot import get_student_info, get_course_info, get_progress
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# ViewSet for the Student model
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# ViewSet for the Course model
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# ViewSet for the Progress model
class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

class ChatbotQueryView(APIView):
    def get(self, request):
        query_type = request.query_params.get('query_type')
        query_value = request.query_params.get('query_value')

        if query_type == 'student_info':
            response = get_student_info(query_value)
        elif query_type == 'course_info':
            response = get_course_info(query_value)
        elif query_type == 'progress':
            student_id, course_name = query_value.split(',')
            response = get_progress(student_id, course_name)
        else:
            response = "Invalid query type."

        return Response({"response": response}, status=status.HTTP_200_OK)
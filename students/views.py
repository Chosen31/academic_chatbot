from rest_framework import viewsets
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Student, Course, Progress
from .serializers import StudentSerializer, CourseSerializer, ProgressSerializer
from .chatbot import get_student_info, get_course_info, get_progress
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

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

# User Registration View
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)

# Login View
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# User Profile View (Requires Authentication)
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def profile_view(request):
    user = request.user
    return Response({"username": user.username})
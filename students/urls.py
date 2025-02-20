from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, CourseViewSet, ProgressViewSet, RegisterView, LoginView, profile_view, ChatbotQueryView
from django.urls import path

# Set up the API router
router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'progress', ProgressViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # API URLs will be prefixed with 'api/'
    path('api/chatbot/', ChatbotQueryView.as_view(), name='chatbot_query'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/profile/', profile_view, name='profile'),

]

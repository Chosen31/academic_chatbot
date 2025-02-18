from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, CourseViewSet, ProgressViewSet
from django.urls import path
from .views import ChatbotQueryView

# Set up the API router
router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'progress', ProgressViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # API URLs will be prefixed with 'api/'
    path('api/chatbot/', ChatbotQueryView.as_view(), name='chatbot_query'),

]

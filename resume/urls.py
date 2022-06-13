from django.urls import path, include
from rest_framework import routers

from resume import views

router = routers.DefaultRouter()
router.register('resume', views.ResumeViewSet, basename='resume')

app_name = 'resume'
urlpatterns = [
    path('', include(router.urls))
]

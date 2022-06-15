from rest_framework import viewsets
from resume.models import Resume, Skill
from resume.serializers import ResumeSerializer, ListResumeSerializer


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ListResumeSerializer
        return self.serializer_class

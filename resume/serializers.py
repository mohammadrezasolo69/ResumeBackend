from django.contrib.auth import get_user_model
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from resume.models import (Resume, Skill, SocialNetwork, Language, CourseCertificate, Project, Education)


# /////////////////////////////////// User Serialize \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email']


# /////////////////////////////////// Skill Serialize \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class NewSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['title', 'level']


# /////////////////////////////////// Social Network Serialize \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class NewSocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = ['title', 'link']


# /////////////////////////////////// Project Serialize \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class NewProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["title", "link", "description", "start_date", "end_date"]


# /////////////////////////////////// Language Serialize \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class NewLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['language', 'level']


# /////////////////////////////////// CourseCertificate Serialize \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class NewCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCertificate
        fields = ["title", "link", "institute", "start_date", "end_date"]


# /////////////////////////////////// Education Serialize \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class NewEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ["grade", "major", "start_date", "end_date"]


# /////////////////////////////////// Resume Serialize \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class ListResumeSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(method_name='get_user')

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Resume
        fields = ['id', 'user', 'title', 'created_at', 'updated_at', ]


class ResumeSerializer(WritableNestedModelSerializer):
    user = UserSerializer(read_only=True)

    skills = NewSkillSerializer(many=True)
    socials = NewSocialNetworkSerializer(many=True)
    languages = NewLanguageSerializer(many=True)
    courses = NewCourseSerializer(many=True)
    projects = NewProjectSerializer(many=True)
    educations = NewEducationSerializer(many=True)

    class Meta:
        model = Resume
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

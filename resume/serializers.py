from django.contrib.auth import get_user_model
from rest_framework import serializers

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
        fields = ['id', 'user', 'title', 'created_at', 'updated_at']


class ResumeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    skills = NewSkillSerializer(many=True)
    social = NewSocialNetworkSerializer(many=True)
    language = NewLanguageSerializer(many=True)
    course = NewCourseSerializer(many=True)
    project = NewProjectSerializer(many=True)
    education = NewEducationSerializer(many=True)

    class Meta:
        model = Resume
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    def create(self, validated_data):
        skills = validated_data.pop('skills')
        social = validated_data.pop('social')
        language = validated_data.pop('language')
        course = validated_data.pop('course')
        project = validated_data.pop('project')
        education = validated_data.pop('education')

        new_resume = Resume.objects.create(**validated_data)

        for skill in skills:
            new_skill = Skill.objects.create(resume=new_resume, **skill)

        for social in social:
            new_socials = SocialNetwork.objects.create(resume=new_resume, **social)

        for language in language:
            new_language = Language.objects.create(resume=new_resume, **language)

        for course in course:
            new_course = CourseCertificate.objects.create(resume=new_resume, **course)

        for project in project:
            new_project = Project.objects.create(resume=new_resume, **project)

        for education in education:
            new_education = Education.objects.create(resume=new_resume, **education)

        return new_resume

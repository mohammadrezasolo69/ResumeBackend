from django.contrib import admin
from resume.models import Resume, Skill, SocialNetwork, CourseCertificate, Project, Language, Education


# //////////////////////// Inline Models \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class SkillInline(admin.TabularInline):
    model = Skill
    fields = ('title', 'level')
    extra = 1

class LanguageInline(admin.TabularInline):
    model = Language
    fields = ('language', 'level')
    extra = 1

class SocialNetworkInline(admin.TabularInline):
    model = SocialNetwork
    fields = ('title', 'link')
    extra = 1


class CourseCertificateInline(admin.TabularInline):
    model = CourseCertificate
    fields = ('title', 'link', 'institute', 'start_date', 'end_date')
    extra = 1


class ProjectInline(admin.TabularInline):
    model = Project
    fields = ('title', 'link', 'description', 'start_date', 'end_date')
    extra = 1


class EducationInline(admin.TabularInline):
    model = Education
    fields = ('grade', 'major', 'start_date', 'end_date')
    extra = 1


# /////////////////////////////////////////////////////////////////////////////

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    inlines = [
        SkillInline, LanguageInline, SocialNetworkInline,
        CourseCertificateInline, ProjectInline, EducationInline
    ]

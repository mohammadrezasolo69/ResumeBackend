from django.contrib import admin
from resume.models import Resume, Skill, SocialNetwork, CourseCertificate, Project, Language, Education


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'resume')


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('language', 'level', 'resume')


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'resume')


@admin.register(CourseCertificate)
class CourseCertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'resume', 'institute', 'start_date', 'end_date')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'resume', 'start_date', 'end_date')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('grade', 'major', 'start_date', 'end_date', 'resume')

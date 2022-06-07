from django.contrib import admin
from resume.models import Resume, Skill


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')


@admin.register(Skill)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'resume')

from django.contrib import admin
from resume.models import Resume, Skill, SocialNetwork


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'resume')


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'resume')

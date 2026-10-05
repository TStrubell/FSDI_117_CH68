# portfolio/admin.py

from django.contrib import admin
from .models import Skill, Project

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level', 'proficiency')
    ordering = ('name',)
    search_fields = ('name', 'category', 'level')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    ordering = ('title',)
    search_fields = ('title', 'category', 'description')
    filter_horizontal = ('skills',)
    prepopulated_fields = {"slug": ("title",)}

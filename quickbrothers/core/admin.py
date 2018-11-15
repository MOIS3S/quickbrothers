from django.contrib import admin
from .models import Project, ProjectImage


class ProjectImageInline(admin.StackedInline):
    model = ProjectImage
    extra = 9


class ProjectAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'address', 'duration']

    inlines = [ProjectImageInline]


admin.site.register(Project, ProjectAdmin)
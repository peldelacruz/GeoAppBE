from django.contrib import admin
from .models import Company, CustomUser, Project, StatusProject, Role, Team
admin.site.register(Company)
admin.site.register(CustomUser)
admin.site.register(Project)
admin.site.register(StatusProject)
admin.site.register(Role)
admin.site.register(Team)
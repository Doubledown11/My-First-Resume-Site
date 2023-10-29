from django.contrib import admin
from .models import User, Experience, Skill, Project, Certification, Education, Volunteer, Blog


# Register your models here.
admin.site.register(User)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Certification)
admin.site.register(Education)
admin.site.register(Volunteer)
admin.site.register(Blog)


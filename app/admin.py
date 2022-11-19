from django.contrib import admin

from .models import Profile, MedicalCondition, UserMedicalCondition

admin.site.register(Profile)
admin.site.register(MedicalCondition)
admin.site.register(UserMedicalCondition)
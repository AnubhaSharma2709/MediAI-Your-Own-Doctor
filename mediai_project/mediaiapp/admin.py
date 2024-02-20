# mediaiapp/admin.py

from django.contrib import admin
from .models import UserProfile, Medical, Ment, Profile

# Register your models here
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_patient', 'is_doctor', 'phoneNumber')

@admin.register(Medical)
class MedicalAdmin(admin.ModelAdmin):
    list_display = ('symptom1', 'symptom2', 'symptom3', 'symptom4', 'symptom5', 'disease', 'medicine', 'patient', 'doctor', 'created_on')

@admin.register(Ment)
class MentAdmin(admin.ModelAdmin):
    list_display = ('approved', 'time', 'patient', 'doctor', 'ment_day', 'medical')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'birth_date', 'region', 'gender', 'country')

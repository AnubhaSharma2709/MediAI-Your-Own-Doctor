from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User as AuthUser


from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add your additional fields here
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    phoneNumber = models.CharField(max_length=200, null=True)
    # Add other profile-related fields

    def __str__(self):
        return self.user.username

class Medical(models.Model):
    symptom1 = models.CharField(max_length=100)
    symptom2 = models.CharField(max_length=100)
    symptom3 = models.CharField(max_length=100)
    symptom4 = models.CharField(max_length=100)
    symptom5 = models.CharField(max_length=100)
    disease = models.CharField(max_length=255)
    medicine = models.CharField(max_length=255)
    patient = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='medical_records')
    doctor = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='medical_prescriptions')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.disease


class Ment(models.Model):
    approved = models.BooleanField(default=False)
    time = models.TimeField()
    patient = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='patient_ments')
    doctor = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='doctor_ments')
    ment_day = models.DateField()
    medical = models.ForeignKey(Medical, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ment for {self.patient} on {self.ment_day}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='default_avatar.jpg')
    birth_date = models.DateField(null=True, blank=True)
    region = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')), blank=True)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

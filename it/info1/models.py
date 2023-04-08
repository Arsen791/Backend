from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_name(models.Model):
    fullname = models.CharField(null=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name = 'User_name'
        verbose_name_plural = 'User_names'

class User_birth(models.Model):
    date_of_birth = models.DateField(null=False)
    place_of_birth = models.CharField(null=False, max_length=255)
    name = models.ForeignKey(User_name, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'User_birth'
        verbose_name_plural = 'User_birth'

class User_info(models.Model):
    specialization = models.CharField(null=False, max_length=255)
    qualification = models.CharField(null=False, max_length=255)
    orga_of_education =  models.CharField(null=False, max_length=255)
    year_of_graduation = models.IntegerField(null=False, default=False)
    specialist_certificate = models.FileField()
    birth = models.ForeignKey(User_birth, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'User_info'
        verbose_name_plural = 'User_info'

class User_work(models.Model):
    address = models.CharField(null=False, max_length=255)
    organizations = models.CharField(null=False, max_length=255)
    position = models.CharField(null=False, max_length=255)
    experience = models.IntegerField(null=False, default=False)
    info = models.ForeignKey(User_info, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'User_work'
        verbose_name_plural = 'User_works'

class Practice(models.Model):
    information = models.FileField(upload_to='images')
    experience = models.IntegerField(null=False, default=False)
    work = models.ForeignKey(User_work, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Practice'
        verbose_name_plural = 'Practices'
    
class Criminal(models.Model):
    criminal = models.FileField(upload_to='images', choices=['yes', 'no'])
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Criminal'
        verbose_name_plural = 'Criminal'

class Medical(models.Model):
    medical_examination = models.FileField(upload_to='images')
    criminal = models.ForeignKey(Criminal, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Medical'
        verbose_name_plural = 'Medical'

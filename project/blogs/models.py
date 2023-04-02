from django.db import models

# Create your models here.
class Oblast(models.Model):
    name = models.CharField(null=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Oblast'
        verbose_name_plural = 'Oblasts'

class City(models.Model):
    name = models.CharField(null=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    oblast = models.ForeignKey(Oblast, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Citys'

class House(models.Model):
    title = models.CharField(null=False, max_length=255)
    description = models.TextField(null=False, blank=True, default='')
    region = models.CharField(null=False, max_length=255)
    street = models.CharField(null=False, max_length=255)
    flat = models.FloatField(null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    City = models.ForeignKey(City, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'House'
        verbose_name_plural = 'Houses'

class Post(models.Model):
    title = models.CharField(null=False, blank=False, max_length=255)
    content = models.TextField(null=False, blank='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='posts')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
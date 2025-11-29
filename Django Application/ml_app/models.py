from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model with user_type field
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='user')
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f"{self.username} ({self.user_type})"
    
    class Meta:
        db_table = 'users'

# Video Upload History
class VideoUploadHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='video_uploads')
    video_name = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    prediction_result = models.CharField(max_length=10, null=True, blank=True)  # REAL or FAKE
    confidence = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.video_name}"
    
    class Meta:
        db_table = 'video_upload_history'
        ordering = ['-upload_date']

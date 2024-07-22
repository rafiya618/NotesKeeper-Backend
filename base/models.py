from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.body[:50]  # Display the first 50 characters of the note in the admin interface

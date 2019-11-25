from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    """modeling blog post"""
    title = models.CharField(max_length=50)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """represent the post"""
        if len(self.text) < 50:
            return self.text
        else:
            return self.text[:50] + '...'

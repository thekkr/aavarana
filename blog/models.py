from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# Create your views here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} | {self.author}"
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your views here.

class PostCategory(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # return reverse("post_detail", kwargs={"pk": self.pk})
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank=True,null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="Cricket")
    likes = models.ManyToManyField(User, related_name='liked_post',blank=True)
    unlikes = models.ManyToManyField(User, related_name='unliked_post',blank=True)
    
    def total_likes(self):
        return self.likes.count()
    
    def total_unlikes(self):
        return self.unlikes.count()
    
    def __str__(self):
        return f"{self.title} | {self.author}"
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
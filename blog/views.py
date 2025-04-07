from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView , DeleteView
from . models import Post
from . forms import PostForm, PostUpdateForm
from django.urls import reverse_lazy

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    ordering = ['-post_date']
    
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_create.html"
    # fields = '__all__'
    
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = "blog/post_update.html"
    # fields = '__all__'
    # fields = ['title','title_tag','body']

class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy('post_list')
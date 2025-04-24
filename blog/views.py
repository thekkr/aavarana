from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView , DeleteView
from . models import Post, PostCategory
from . forms import PostForm, PostUpdateForm, PostCategoryForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

def like_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        post.unlikes.remove(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))

def unlike_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.user in post.unlikes.all():
        post.unlikes.remove(request.user)
    else:
        post.unlikes.add(request.user)
        post.likes.remove(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))

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

class PostCategoryAddView(CreateView):
    model = PostCategory
    form_class = PostCategoryForm
    template_name = "blog/add_post_category.html"
    # fields = '__all__'

class PostCategoryListView(ListView):
    model = Post
    template_name = "blog/post_category_list.html"
    
    def get_queryset(self):
        category = self.kwargs.get('category')
        return Post.objects.filter(category=category.replace('-',' ').title())

    
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
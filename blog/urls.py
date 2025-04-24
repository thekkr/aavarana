from django.urls import path
from . import views

urlpatterns = [
    path('post_list/', views.PostListView.as_view(),name="post_list"),
    path('post_detail/<int:pk>', views.PostDetailView.as_view(),name="post_detail"),
    path('post_create/', views.PostCreateView.as_view(),name="post_create"),
    path('post_update/<int:pk>', views.PostUpdateView.as_view(),name="post_update"),
    path('post_delete/<int:pk>', views.PostDeleteView.as_view(),name="post_delete"),
    path('post_category_list/<str:category>', views.PostCategoryListView.as_view(),name="post_category_list"),
    path('add_post_category/', views.PostCategoryAddView.as_view(),name="add_post_category"),
    path('like_post/<int:pk>', views.like_view, name="like_post"),
    path('unlike_post/<int:pk>', views.unlike_view, name="unlike_post"),
]
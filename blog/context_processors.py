from .models import PostCategory

def category_list(request):
    return {'categories':PostCategory.objects.all()}
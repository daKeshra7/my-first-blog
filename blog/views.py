from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    return render(request,'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})


# <p>published: today</p>
#         <h2><a href=""> My first Post</a></h2>
#         <p>Everything was light and the shadow looked dim. Even
#     in the midst of all other galaxy, the sun is deemed as a lone simple
#     stpython3ar yet it outshine the rest of the milky way.


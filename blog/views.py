from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView


class PostListView(ListView):
    queryset = Post.published.all() 
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'blog/post/list.html'
    print(queryset)

    

def post_details(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
    
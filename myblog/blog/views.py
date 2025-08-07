# blog/views.py
from django.http import HttpResponse
from .models import Post

def home(request):
    posts = Post.objects.all()
    post_list = "<h1>Мой блог</h1>"
    for post in posts:
        post_list += f"<h2>{post.title}</h2><p>{post.content}</p><p>Создано: {post.created_at}</p>"
    return HttpResponse(post_list)
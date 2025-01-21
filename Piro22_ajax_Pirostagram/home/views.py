from django.shortcuts import render

# Create your views here.

def index(request):
    posts = Post.objects.all()

    for post in posts:
        comments = Comment.objects.filter(post=post)
        post.comments = comments

    return render(request, 'home/index.html', {'posts': posts})

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Post, Comment

@csrf_exempt
def like(request):

    data = json.loads(request.body)
    
    post_id = data.get('post_id')
    
    post = Post.objects.get(id=post_id)
    
    post.likes += 1
    
    post.save()
    
    return JsonResponse({ 'id': post.id, 'likes': post.likes })

@csrf_exempt
def comment_register(request):

    data = json.loads(request.body)

    post_id = data['post_id']
    comment_content = data['comment_content']
    
    post = Post.objects.get(id=post_id)
    
    newComment = Comment.objects.create(content=comment_content, post=post, creator=request.user)

    return JsonResponse({
        'post_id': post_id, 
        'comment':{
            'id': newComment.id,
            'content': newComment.content,
            'creator': {
                'username': newComment.creator.username
            }
        }})

@csrf_exempt
def comment_delete(request):
    data = json.loads(request.body)

    comment_id = data['comment_id']
    
    comment = Comment.objects.get(id=comment_id)
    
    comment.delete()

    return JsonResponse({'comment_id': comment_id})
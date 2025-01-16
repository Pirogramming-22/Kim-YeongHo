from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post
from DevTool.models import Devtool


# Create your views here.

def ideaManage(request):
    if request.method == 'GET':
        sort_by = request.GET.get('sort_by','title')
        posts = Post.objects.order_by(sort_by)
        return render(request , 'post/index.html' , {'posts' : posts})
    else:
        posts=Post.objects.all()
        return render(request , 'post/index.html' , {'posts' : posts})

def ideaRegister(request):
    if(request.method == 'POST'):
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('post:ideaDetail' , pk =post.pk)
    else:
        form=PostForm()
    
    return render(request , 'post/create.html' , {'form' : form})

def ideaDetail(request,pk):
    if request.method == 'GET':
        post = Post.objects.get(id=pk)
        return render(request , 'post/detail.html' , {'post':post})
    elif request.method == 'POST':
        post= Post.objects.get(id=pk)
        post.title =request.POST['title']
        if 'image' in request.FILES:
            post.image =request.FILES['image'] 
        post.explanation =request.POST['explanation']
        post.interest =request.POST['interest']
        expectedToolid = request.POST['expectedTool']
        post.expectedTool = Devtool.objects.get(id=expectedToolid)
        post.save()
        return render(request , 'post/detail.html' , {'post':post})
    
def ideaDelete(request,pk):
    form = Post.objects.get(id=pk)
    form.delete()
    return redirect('post:ideaManage')

def ideaUpdate(request , pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    ctx={
        'post' : post,
        'form' : form,
        'pk' : pk
    }
    return render(request , 'post/update.html' ,ctx)

from django.http import JsonResponse  # JsonResponse import
from django.views.decorators.http import require_POST
from .models import Post

@require_POST  # POST 요청만 허용
def toggle_star(request, pk):
    try:
        post = Post.objects.get(pk=pk)  # pk로 Post 객체 가져오기
        post.star = not post.star  # 찜 상태 반전 (True ↔ False)
        post.save()
        return JsonResponse({'success': True, 'starred': post.star})  # JSON 응답 반환
    except Post.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Post not found'})

def plusInterest(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.interest += 1  # 관심도 증가
        post.save()
        return JsonResponse({'success': True, 'interest': post.interest})
    return JsonResponse({'success': False, 'error': 'Invalid request'})

def minusInterest(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.interest -= 1  # 관심도 감소
        post.save()
        return JsonResponse({'success': True, 'interest': post.interest})
    return JsonResponse({'success': False, 'error': 'Invalid request'})

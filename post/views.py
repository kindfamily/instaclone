from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from django.contrib import messages


def post_list(request):

    post_list = Post.objects.all()
    
    if request.user.is_authenticated:
        username = request.user
        user = get_object_or_404(get_user_model(), username=username)
        user_profile = user.profile
        
        return render(request, 'post/post_list.html', {
            'user_profile': user_profile,
            'posts': post_list,
        })
    else:
        return render(request, 'post/post_list.html',{
            'posts': post_list,
        })
    
@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            # post.tag_save()
            messages.info(request, '새 글이 등록되었습니다')
            return redirect('post:post_list')
    else:
        form = PostForm()
    return render(request, 'post/post_new.html', {
        'form': form,
    })

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        messages.warning(request, '잘못된 접근입니다')
        return redirect('post:post_list')
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            # post.tag_set.clear()
            # post.tag_save()
            messages.success(request, '수정완료')
            return redirect('post:post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'post/post_edit.html', {
        'post': post,
        'form': form,
    })

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user or request.method == 'GET':
        messages.warning(request, '잘못된 접근입니다.')
        return redirect('post:post_list')

    if request.method == 'POST':
        post.delete()
        messages.success(request, '삭제완료')
        return redirect('post:post_list')








            
            
            
            
            
            
            
            
            
            
            
            
            
            
            







        
    
    

















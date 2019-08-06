from django.contrib import messages

from django.contrib.auth import get_user_model
import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from django.views.decorators.http import require_POST
from django.db.models import Count



from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post, Like




def post_list(request):

    
    post_list = Post.objects.all() 


    paginator = Paginator(post_list, 3)
    page_num = request.POST.get('page')

    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    if request.is_ajax():  # Ajax request 여부 확인
        return render(request, 'post/post_list_ajax.html', {
            'posts': posts,
            'comment_form': comment_form,
        })

    

    return render(request, 'post/post_list.html', {
        'posts': posts,
    })


@login_required
@require_POST  # 해당 뷰는 POST method 만 받는다.
def post_like(request):
    pk = request.POST.get('pk', None)
    post = get_object_or_404(Post, pk=pk)
    post_like, post_like_created = post.like_set.get_or_create(user=request.user)

    if not post_like_created:
        post_like.delete()
        message = "좋아요 취소"
    else:
        message = "좋아요"

    context = {'like_count': post.like_count,
               'message': message,
               'nickname': request.user.profile.nickname}

    return HttpResponse(json.dumps(context), content_type="application/json")
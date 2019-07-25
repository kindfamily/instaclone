from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post

def post_list(request):
    post_list = Post.objects.all()
    
    paginator = Paginator(post_list, 3)
    page_num = request.POST.get('page')
    
    try:
        posts = paginator.page(page_num)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(pagintor.num_pages)
        
    return render(request, 'post/post_list.html', {
        'posts': posts,
    })
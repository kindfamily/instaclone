from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import logout as django_logout
from .forms import SignupForm, LoginForm
from .models import Profile, Follow

import json
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST



def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:login')
    else:
        form = SignupForm()
        
        
    if request.is_ajax():
        profile, created_at = Profile.objects.get_or_create(user=user_id)

        if created_at:
            message = '이미 가입된 사용자입니다!'
            status = 1
        else:
            profile.delete()
            message = '회원가입 간입가능'
            status = 0

        context = {
            'message': message,
            'status': status,
        }
        return HttpResponse(json.dumps(context), content_type="application/json")
        
        
        return render(request, 'post/post_list_ajax.html', {
            'posts': posts,
            'comment_form': comment_form,
        })  
        
    return render(request, 'accounts/signup.html', {
        'form': form,
    })

def login_check(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        
        user = authenticate(username=name, password=pwd)
        
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'accounts/login_fail.html')
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {"form":form})
    
def logout(request):
    django_logout(request)
    return redirect("/")

@login_required
@require_POST
def follow(request):
    from_user = request.user.profile
    pk = request.POST.get('pk')
    to_user = get_object_or_404(Profile, pk=pk)
    follow, created = Follow.objects.get_or_create(from_user=from_user, to_user=to_user)
    
    if created:
        message = '팔로우 시작!'
        status = 1
    else:
        follow.delete()
        message = '팔로우 취소'
        status = 0
        
    context = {
        'message': message,
        'status': status,
    }
    return HttpResponse(json.dumps(context), content_type="application/json")
    
            
            
            
            
            
            
            
            
            
            
            
            

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    username = forms.CharField(label='사용자이름', widget=forms.TextInput(attrs={
        'pattern': '[a-zA-Z0-9]+',
        'title': '특수문자, 공백 입력안됨',
    }))
    
    nickname = forms.CharField(label='닉네임')
    picture = forms.ImageField(label='프로필 사진')
    
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)
        
    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        if Profile.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError('이미 존재하는 별명 이에요')
        return nickname
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        User = get_user_model()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('이미 사용중인 이메일 이에요')
        return email
    
    def clean_picture(self):
        picture = self.cleaned_data.get('picture')
        if not picture:
            picture = None
        return picture
    
    def save(self):
        user = super().save()
        Profile.objects.create(
            user=user,
            nickname=self.cleaned_data['nickname'],
            picture=self.cleaned_date['picture'],)
        return user
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
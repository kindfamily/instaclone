from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
    
    path('', post_list, name='post_list'),
    path('like', post_like, name='post_like'),
    
    
]
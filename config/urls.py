from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

# 작성 2
from django.shortcuts import redirect



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('post/', include('post.urls')),
    
    # 작성1
    path('', lambda r: redirect('post:post_list'), name='root'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
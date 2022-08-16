from django.urls import path
from blog import views



urlpatterns = [
   path('blog_post/', views.blog_post, name='blog_post'),
   path('post_detail/<slug:slug>/', views.post_detail, name='post_detail'),
] 
# +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


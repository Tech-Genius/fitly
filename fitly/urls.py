from django.urls import path
from fitly import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   path('', views.index, name='index'),
   # path('profile/<int:pk>', views.profile, name='profile'),
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


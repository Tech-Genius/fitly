from django.urls import path
from thread import views


urlpatterns = [
   path('active_thread/<int:pk>/', views.active_thread, name='active_thread'),
   path('post_thread', views.post_thread, name='post_thread'),
   path('community', views.community, name='community'),
   path('delete_thread/<int:pk>/', views.delete_thread, name='delete_thread'),
   
]

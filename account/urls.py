from django.urls import path
from account import views


urlpatterns = [
   path('logout', views.userlogout, name='logout'),
   path('login/', views.loginpage, name='login'),
   path('register', views.register, name='register'),
]

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.




class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to= "blog_images")
    

    class Meta:
        ordering = ['-date_added']
class Comment(models.Model): 
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name ='comments')
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField() 
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added'] 
   


    

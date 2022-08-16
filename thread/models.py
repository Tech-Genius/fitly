from django.db import models
# Create your models here.
from django.contrib.auth.models import User



class Thread(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=600)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=True) 
    # slug = models.SlugField(default='', unique_for_date='date', blank=True)


    class Meta:
        ordering = ['-date']
        

    def __str__(self):
        return str(self.user)


class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread,related_name='replies', on_delete=models.CASCADE)
    content = models.CharField(max_length=600)
    date_added = models.DateTimeField(auto_now_add=True)



    class Meta:
        ordering = ['-date_added'] 


    def __str__(self):
        return str(self.date_added)    
          



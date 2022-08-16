from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Intros(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    img = models.ImageField(null=True, blank=False, upload_to= "images/")

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "intros"
        verbose_name_plural = "intros"


class Services(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    img = models.ImageField(null=True, blank=False, upload_to= "images/")

    def __str__(self):
        return self.title



    class Meta:
        verbose_name = "services"
        verbose_name_plural = "services"            








class Trainees(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    img = models.ImageField(null=True, blank=False, upload_to= "images/")

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "trainees"
        verbose_name_plural = "trainees"      



     






class Testimonials(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=100, blank=True)
    img = models.ImageField(null=True, blank=False, upload_to= "images/")

    def __str__(self):
        return self.name



    class Meta:
        verbose_name = "testimonials"
        verbose_name_plural = "testimonials"       







class Footer(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    gmail = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    copywrite_year = models.CharField(max_length=200)

    def __str__(self):
        return self.copywrite_year  



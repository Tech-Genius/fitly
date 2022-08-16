from django.shortcuts import render
from . models import *
from . models import Services
from account import views

# Create your views here.
def index(request):
    intros = Intros.objects.all()
    services = Services.objects.all()
    trainees = Trainees.objects.all()
    testimonials = Testimonials.objects.all()
    footers = Footer.objects.all()
    context = {
        'intros' : intros, 
        'services': services,
        'trainees': trainees,
        'testimonials': testimonials,
        'footers': footers,

    }
    return render(request, 'fitly/index.html', context)





# def profile(request, pk):
    
#     return render(request, 'fitly/profile.html', pk)   
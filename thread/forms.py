from django import forms
from . models import *




class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title','content']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']        
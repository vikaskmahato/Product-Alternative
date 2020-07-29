from django import forms
from .models import Post

class Postform(forms.ModelForm):
    class Meta:
        model=Post
        fields=('content','image')
        widgets={ 'content':forms.Textarea(attrs={'class': 'form-control'}),
                  }
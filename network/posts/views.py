from django.shortcuts import render
from .models import Post
from accounts.models import Profile
from .forms import Postform

# Create your views here.
def createpost(request):
    p=Post.objects.all()
    form=Postform(request.POST or None, request.FILES or None)
    profile=Profile.objects.get(user=request.user)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.author=profile
        instance.save()
        form=Postform()
    return render(request, 'posts/post.html', {'posts':p,'form':form,'profile':profile})
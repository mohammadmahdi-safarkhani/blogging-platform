from django.shortcuts import render
from .models import Post
from account.models import CustomUser

# Create your views here.

def home_page(request):
    post = Post.objects.all()
    return render(request,'base/home_page.html',{'post':post})
#-----------------------------------------------------
def add_post(request):
    user = CustomUser.objects.all()
    return render(request,'post/add_post.html',{'user':user})





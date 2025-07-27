from django.shortcuts import render,redirect
from .models import Post
from account.models import CustomUser
from django.contrib import messages
# Create your views here.

def home_page(request):
    post = Post.objects.all()
    return render(request,'base/home_page.html',{'post':post})
#-----------------------------------------------------
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = CustomUser.objects.get(email=request.user.email)
            post = Post
            title = request.POST['title']
            auther = user
            content = request.POST['content']
            if 'published' in request.POST:
                published = True
            else:
                published = False

            new_post = post(title = title, auther = auther, content = content, published = published)
            new_post.save()
            messages.success(request,'post added successfully')
            return redirect('home')
        else:
            return render(request,'post/add_post.html')
    else:
         return render(request,'post/add_post.html')













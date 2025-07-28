from django.shortcuts import render,redirect
from .models import Post
from account.models import CustomUser
from django.contrib import messages
from django.utils.text import slugify
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
#-----------------------------------------------------
def dashboard(request, username):
    if not request.user.is_authenticated:
        redirect('login')
    user = CustomUser.objects.get(username=username)
    post = Post.objects.filter(auther=user)
    return render(request,'post/dashboard.html',{'user':user,'post':post})
#-----------------------------------------------------

def edit_post(request, pk):
    if request.user.is_authenticated:
        post = Post.objects.get(id=pk)

        if request.method == 'POST':
            title = request.POST['title']
            content = request.POST['content']
            published = 'published' in request.POST

            # Update the existing post
            post.title = title
            post.content = content
            post.published = published
            post.slug = slugify(title)
            post.save()
            messages.success(request,'post edited successfully')

            return redirect('dashboard', username=request.user.username)

        return render(request, 'post/edit_post.html', {'post': post})


def delete_post(request, pk):
    if request.user.is_authenticated:
        post = Post.objects.get(id=pk)
        if request.method == 'POST':

            post.delete()
            messages.success(request,'post deleted successfully')
            return redirect('dashboard', username=request.user.username)


    return redirect('dashboard', username=request.user.username)

def post_page(request, slug):
    chosen_post = Post.objects.filter(slug=slug) 
    return render(request, 'post/post_page.html', {'chosen_post': chosen_post})







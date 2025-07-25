from django.shortcuts import render, redirect
from .forms import UserForm,UserLoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.



def signupuser(request):
    if request.method == 'POST':
        new_form = UserForm(request.POST)
        if new_form.is_valid():
            user = new_form.save()
            login(request, user)
            messages.success(request, "Account created! You're now logged in.")
            return redirect('home')
    else:
        return render(request, 'auth/signup.html',{'form':UserForm})
    return render(request, 'auth/signup.html',{'form':UserForm})

#--------------------------------------------------------------------------------------

def loginuser(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You're now logged in.")
                return redirect('home')
            else:
                messages.error(request, "Invalid credentials.")
        else:
            messages.error(request, "Form not valid.")
        return redirect('login')  # this should be outside the form check
    else:
        return render(request, 'auth/login.html', {'form': UserLoginForm()})

#--------------------------------------------------------------------------------------
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "You're now logged out.")
        return redirect('home')
    else:
        return render(request, 'auth/login.html', {'form': UserLoginForm()})

    
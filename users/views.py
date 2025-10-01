from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('menu')  # redirect after login
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'users/login.html')
#XD
def logout_view(request):
    logout(request)
    messages.info(request, "You’ve been logged out.")
    return redirect('login_view')
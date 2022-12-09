from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages #flash messages
from .models import User #User modal
from django.contrib.auth import authenticate, login, logout #for authentication
# from .forms import RegisterForm
from .forms import RegisterForm

def loginPage(request):
    if request.user.is_authenticated:   
        return render(request, 'facultyManagementApp/index.html')  
    return render(request, 'login.html')

def validateLogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
        user = User.objects.get(username=username)
    except:
        messages.warning(request, 'Account doesnt exist.')
    else:
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse(f'hello {username}')  
        else: 
            messages.warning(request, 'Invalid password.')

    return redirect('login')

def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request):
    form = RegisterForm()
    if request.user.is_authenticated:   
        return render(request, 'facultyManagementApp/index.html') 
    context = {'form': form}
    
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.set_password(request.POST['password'])
            user.save() 
            return redirect('login')
        else:
            messages.error(request, "an error has occured")
    return render(request, 'register.html', context)


    
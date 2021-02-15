from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm


# Create your views here.
def home(request):
	if request.user.is_authenticated:
		return render(request, 'authenticate/home.html', {})
	else:
		return redirect('login')

def login_user(request):
	if request.method == 'POST':
	    username = request.POST['username']
	    password = request.POST['password']
	    user = authenticate(request, username=username, password=password)
	    if user is not None:
	        login(request, user)
	        # Redirect to a success page.
	        messages.success(request, ('You have been logged in!'))
	        return redirect('home')
	    else:
	        # Return an 'invalid login' error message.
	        messages.success(request, ('Error! Incorrect password. Try again!'))
	        return redirect('login')
	else:
		return render(request, 'authenticate/login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request, ('Log out successful!'))
	return redirect('login')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(request, username=username, password=password)
			login(request, user)
			messages.success(request, ('Enregistrement effectué avec succès!'))
			return redirect('home')
	else:
		form = SignUpForm()
	context = {'form': form}
	return render(request, 'authenticate/register.html', context)

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView
from .models import Profile
from .forms import ProfileForm, UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data['password'])
			new_user.save()
			Profile.objects.create(user=new_user)
			messages.success(request, 'Registration successful. Please log in.')
			return redirect('users:login')
	else:
		form = UserRegistrationForm()
	return render(request, 'users/register.html', {'form': form})

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('core:home')
	else:
		form = AuthenticationForm()
	return render(request, 'users/login.html', {'form': form})

def logout_view(request):
	logout(request)
	return redirect('core:home')

class ProfileDetailView(DetailView):
	model = Profile
	template_name = 'users/profile_detail.html'
	context_object_name = 'profile'

class ProfileUpdateView(UpdateView):
	model = Profile
	form_class = ProfileForm
	template_name = 'users/profile_form.html'
	success_url = '/users/profile/'

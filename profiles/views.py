# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from profiles.forms import RegistrationForm
from django.urls import reverse
from .models import Item
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

def sign_in(request):
	if request.user.is_authenticated:
		return redirect('/')
	context = {}
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username = username, password = password)

		if user:
			login(request, user)
			return redirect('/')
		else:
			context['error'] = 'Invalid username of password'
			context['username'] = username
	
	return render(request, 'profiles/registration/login.html', context = context)

def sign_up(request):
	if request.user.is_authenticated:
		return redirect('/')
	context = {}
	form = RegistrationForm()
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			context['success'] = True
	else:
		form = RegistrationForm()
	context['form'] = form
	return render(request, 'profiles/registration/signup.html',context = context)

def sign_out(request):
	logout(request)
	return redirect('/')

class ItemCreate(CreateView):
	model = Item
	fields = ['owner','item_name', 'description', 'price','picture']

	def get_initial(self):
		return {'owner': self.request.user }



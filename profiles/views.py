# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from profiles.forms import RegistrationForm,ItemForm
from django.urls import reverse
from .models import Item

def add_item(request):
	if not request.user.is_authenticated():
		return redirect('/')
	else:
		form = ItemForm(request.POST)

	context = {
		'form':form
	}
	return render(request,'add_item.html', context)


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
	return render(request, 'registration/login.html', context = context)

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
	return render(request, 'registration/signup.html',context = context)

def sign_out(request):
	logout(request)
	return redirect('/')

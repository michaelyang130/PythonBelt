from django.shortcuts import render, redirect
from .models import User, Product
from django.contrib import messages


def index(request):
	print('aaa' * 100)
	return render(request, 'wish/index.html')


def register(request):
	print('bbb' * 100)
	user = User.objects.register(request.POST)
	if user[0]:
		request.session['user'] = {
			'id' : user[1].id,
			'name' : user[1].name,
			'username' : user[1].username
		}
		return redirect('/dashboard')
	else:
		for error in user[1]:
			messages.error(request, error)
		return redirect('/')

def login(request):
	print('ccc' * 100)
	user = User.objects.login(request.POST)
	if user[0]:
		request.session['user'] = {
			'id' : user[1].id,
			'name' : user[1].name,
			'username' : user[1].username
		}
		return redirect('/dashboard')
	else:
		for error in user[1]:
			messages.error(request, error)
		return redirect('/')


def dashboard(request):
	print('ddd' * 100)
	user = User.objects.get(id = request.session['user']['id'])
	context = {
		'myitems' : Product.objects.filter(useritem = user)|Product.objects.filter(shareditem__id = user.id),
		'othersitems' : Product.objects.exclude(useritem = user).exclude(shareditem__id = user.id)
	}
	return render(request, 'wish/dashboard.html', context)


def logout(request):
	print('eee' * 100)
	request.session.clear()
	return redirect('/')


def add(request):
	print('fff' * 100)
	return render(request, 'wish/add.html')


def create(request):
	print('ggg' * 100)
	item = Product.objects.create_item(request.POST, request.session['user']['id'])
	if item[0]:
		return redirect('/dashboard')
	else:
		for error in item[1]:
			messages.error(request, error)
		return redirect('/add')


def product(request, id):
	context = {
		'item' : Product.objects.get(id = id)
	}
	return render(request, 'wish/product.html', context)


def wishlist(request, id):
	user = User.objects.get(id = request.session['user']['id'])
	item = Product.objects.get(id = id)
	item.shareditem.add(user)
	return redirect('/dashboard')


def destroy(request, id):
	item = Product.objects.get(id = id)
	item.delete()
	return redirect('/dashboard')








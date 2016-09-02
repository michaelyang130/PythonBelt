from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import re
from django.contrib import messages
import bcrypt
from datetime import datetime, timedelta, time, date
from time import strftime



class UserManager(models.Manager):
	def register(self, data):
		error = []
		now = strftime("%Y-%m-%d")
		if len(data['name']) < 3:
			error.append('Name must have at least 3 characters')
		if (data['name'].strip().replace(' ','',1).isalpha() == False):
			error.append('Name cannot contain any numbers')
		if len(data['username']) < 3:
			error.append('Username must have at least 3 characters')
		if len(data['password']) < 8:
			error.append('Password must have at least 8 characters')
		if not (data['hire_date'] < now):
			error.append('You have not been hired yet')

		user = self.filter(username = data['username'])
		if user:
			error.append('This username already exists')
		if data['password'] != data['confirm_password']:
			error.append('These passwords do not match')

		if error:
			return (False, error)
		else:
			hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
			user = self.create(name = data['name'], username = data['username'], password = hashed, hire_date = data['hire_date'])
			return (True, user)
		
	def login(self, data):
		error = []
		user = self.filter(username = data['username'])
		if user:
			if bcrypt.hashpw(data['password'].encode('utf-8'), user[0].password.encode('utf-8')) == user[0].password:
				return(True, user[0])
		else:
			error.append('Invalid Login')
			return (False, error)


class ItemManager(models.Manager):
	def create_item(self, coffee, user_id):
		errors = []
		if len(coffee['item']) < 0:
			errors.append('Must enter an item! Field cannot be blank!')
		if len(coffee['item']) < 3:
			errors.append('Item must have more than 3 characters')

		if errors:
			return(False, errors)
		else:
			item = self.create(useritem = User.objects.get(id = user_id), item = coffee['item'])
			return (True, coffee)





class User(models.Model):
	name = models.CharField(max_length = 100)
	username = models.CharField(max_length = 100)
	password = models.CharField(max_length = 100)
	hire_date = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()


class Product(models.Model):
	item = models.CharField(max_length = 100)
	useritem = models.ForeignKey(User, related_name = 'useritem')
	shareditem = models.ManyToManyField(User, related_name = 'shareditem')
	dated_added = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ItemManager()





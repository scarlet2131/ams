from django.shortcuts import render
from .models import *

from django.http import *
import re
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime
from django.utils import timezone

@csrf_exempt
def register(request):
	# fields=['name','username','password','phone_no','address','user_type']

	
	if request.method=='POST':
		print("add professor")
		userInstance = professor()
		name = request.POST.get("username") 
		password = request.POST.get("password")
		email = request.POST.get("email")
		if(len(name)==0 or len(email)==0 or len(password)==0):
			return render(request,'register.html',{"error_message":"Some Fields may be empty"} )
		print(name,password,email)
		isPresent=professor.objects.filter(name=name,email=email)
		if not isPresent:
			userInstance.name=name
			userInstance.password=password
			userInstance.email=email
			userInstance.save()
			return render(request,'register.html',{"register":"Successfully Registered Professor: "+name} )
		else:
			return render(request,'register.html',{"error_message":"Professor: {} already present.".format(name)} )

	return render(request,'register.html')

@csrf_exempt
def login(request):
	print("login")
	if request.method =="POST":
		name = request.POST.get("name")
		password = request.POST.get("password")
		print(name,password)
		isPresent=professor.objects.filter(name=name,password=password)
		if isPresent:
			return HttpResponseRedirect('/main')
		else:
			return render(request,'login.html',{"error_message": "Password/Username may be wrong"})
	return render(request,'login.html')
		


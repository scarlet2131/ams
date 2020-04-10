from django.shortcuts import render
from .models import *

from django.http import *
import re
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime
from django.utils import timezone
from pyqrcode import QRCode 
import pyqrcode 
import datetime 


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
		name = request.POST.get("username")
		password = request.POST.get("password")
		print(name,password)
		isPresent=professor.objects.filter(name=name,password=password)
		if isPresent:
			return HttpResponseRedirect('/main')
		else:
			return render(request,'login.html',{"error_message": "Password/Username may be wrong"})
	return render(request,'login.html')

@csrf_exempt
def main(request):
	return render(request,'main.html')

def qrpage(request):
	file_name=""
	course_id=request.POST.get("Course_ID")
	t=str(datetime.datetime.now()).split(" ")[0]
	s = "www."+course_id+t+"org"
	url = pyqrcode.create(s)  
	file_name="qr/"+course_id+t+".svg"
	url.svg("login/static/"+file_name, scale = 8) 
	return render(request,'qrpage.html',{"qrCode": file_name})
	
		


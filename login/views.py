from django.shortcuts import render
from .models import *

from django.http import *
import re
from django.views.decorators.csrf import csrf_exempt


from datetime import datetime
from django.utils import timezone
from login.qrCode import qrCode
import ams.settings as settings
from login.capture import capture

from firebase import firebase  
import json
from datetime import date



@csrf_exempt
def register(request):

	if request.method=='POST':
		print("add professor")
		# print(request)
		userInstance = professor()
		name = request.POST.get("username")
		password = request.POST.get("password")
		email = request.POST.get("email")
		if (len(name)==0 or len(email)==0 or len(password)==0):
			return render(request,'register.html',{"error_message":"Some Fields may be empty"} )
		print(name,password,email)
		isPresent = professor.objects.filter(name=name,email=email)

		loc = firebase.FirebaseApplication('https://amsproject-fe165.firebaseio.com/', None)
		dbLOC = '/Users/'
		result = loc.get(dbLOC, '')
		print(result)
		# check if the student has already marked Attendance
		already = False
		if result is not None :
			for p in result:
				if result[p]['email'] == email:
					already = True
					break
		if not already:
			data = {
				"name":name,
				"email":email,
				"password":password,
			}
			result = loc.post(dbLOC,data)
			return render(request,'register.html',{"register":"Successfully Registered Professor: "+name} )
		else:
			return render(request,'register.html',{"error_message":"Professor: {} already present.".format(name)} )
		
	return render(request,'register.html')

@csrf_exempt
def login(request):

	print("login")
	if request.method=='POST':
		name = request.POST.get("username")
		password = request.POST.get("password")
		print(name,password)
		isPresent = professor.objects.filter(name=name,password=password)


		loc = firebase.FirebaseApplication('https://amsproject-fe165.firebaseio.com/', None)
		dbLOC = '/Users/'
		result = loc.get(dbLOC, '')
		print(result)
		# check if the student has already marked Attendance
		already = False
		if result is not None :
			for p in result:
				if result[p]['email'] == email:
					already = True
					break
		if already:
			return HttpResponseRedirect('/course')
		else:
			return render(request,'login.html',{"error_message":"Password/Username may be Wrong"} )
	return render(request,'login.html')

@csrf_exempt
def Form(request):

	print("login")
	if request.method=='POST':
		email = request.POST.get("username")
		password = request.POST.get("password")

		


		loc = firebase.FirebaseApplication('https://amsproject-fe165.firebaseio.com/', None)
		dbLOC = '/Users/'
		result = loc.get(dbLOC, '')
		print(result)
		# check if the student has already marked Attendance
		already = False
		if result is not None :
			for p in result:
				if result[p]['email'] == email:
					already = True
					break
		if already:
			return HttpResponseRedirect('/course')
		else:
			return render(request,'login.html',{"error_message":"Password/Username may be Wrong"} )
	return render(request,'login.html')

@csrf_exempt
def course(request):

	print("Inside Course")
	return render(request,'chooseCourse.html')

def main(request):

	print("Inside MAIN+QR")
	course = request.POST.get('course')
	qrObject = qrCode(course)
	createdQr = qrObject.genQR()
	print(course)
	print(createdQr)
	today = date.today();
	return render(request,'main.html',{'qrCode':createdQr,'course':course,'date':str(today)})



#following is the WebCam recognition
def imageRec(request):
	REC = capture()
	yourName = REC.process()
	name = "Unknown"
	yourImage = "YourImage"
	if yourName!="Unknown":
		print( yourName.split("_") )
		name = yourName.split("_")[0] + " " + yourName.split("_")[1]
		roll = yourName.split("_")[2]
		print("Identified as ",yourName)

		loc = firebase.FirebaseApplication('https://amsproject-fe165.firebaseio.com/', None)
		today = date.today()
		dbLOC = '/attendance/'+str(today)
		result = loc.get(dbLOC, '')
		print(result)
		# check if the student has already marked Attendance
		already = False
		if result is not None :
			for p in result:
				if result[p]['name'] == name:
					already = True
					break
		if not already:
			if yourName!="Unknown":
				data = {
					"name":name,
					"time":roll,
					"status":"P"
				}
				result = loc.post(dbLOC,data)
				print(result)
		yourImage = "YourImage"
	return render(request,'showYourImage.html',{'yourName':name,'yourImage':yourImage})
	

def pingDB(request):
	loc = firebase.FirebaseApplication('https://amsproject-fe165.firebaseio.com/', None)
	today = date.today()
	dbLOC = '/attendance/'+str(today)
	result = loc.get(dbLOC, '')
	# print(result)
	marked = []
	if result!=None:
		for p in result:
			if result[p]['status']=='P':
				marked.append( {'name':result[p]['name'],'roll':result[p]['time']} )
	return JsonResponse(marked,safe=False)


def present(x,result):
	for p in result:
		if p==x:
			return True
	return False

def closeAttendance(request):
	loc = firebase.FirebaseApplication('https://amsproject-fe165.firebaseio.com/', None)
	student = json.loads(request.POST.get('student'))
	# print(student)
	today = date.today()
	dbLOC = '/attendance/'+str(today)
	result = loc.get(dbLOC, '')
	name = []
	if result!=None:
		for p in result:
			name.append(result[p]['name'])
	
	for s in student['marked']:
		if not present(s['name'],name):
			data = {
				"name":s['name'],
				"time":s["roll"],
				"status":s["status"]
			}
			result = loc.post(dbLOC,data)
	data = []
	data.append({"success":True})
	return JsonResponse(data,safe=False)
	

# ajax functions
@csrf_exempt
def validate_username(request):
	# print(request)
	username = request.POST['str']
	print(username)
	already = False
	if len(username)==0:
		already=True

	loc = firebase.FirebaseApplication('https://amsproject-fe165.firebaseio.com/', None)
	dbLOC = '/Users/'
	Users = loc.get(dbLOC, '')
	if Users!=None:
		for p in Users:
			if Users[p]['name']== username:
				already= True
				break

	data = {
	   'is_taken': already
	}

	return JsonResponse(data)



@csrf_exempt
def validate_email(request):
	# print(request)
	email = request.POST['str']
	print(email)
	already = False
	if len(email)==0:
		already= True
	loc = firebase.FirebaseApplication('https://amsproject-fe165.firebaseio.com/', None)
	dbLOC = '/Users/'
	Users = loc.get(dbLOC, '')
	if Users!=None:
		for p in Users:
			if Users[p]['email']== email:
				already= True
				break

	regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
	if not re.search(regex,email):
		already = True   
      
	data = {
	   'is_taken': already
	}

	return JsonResponse(data)


		
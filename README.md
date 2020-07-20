# Attendance Management System

To develop an interactive online application which can make the job of taking and maintaining
attendance faster and reliable.
The main aim of this project is to reduce Human effort.

Technologies used: HTML5, CSS3, AJAX,Django ,Firebase, Machine learning,Google Maps.

## Installation	
Install python3
Install Django 3.0
Install all the modules in requirements.txt.
## Requirements
Written in Requirements.txt

## Steps to use the attendance management system
Before running the project please make sure that the credentials are set in console.developers.google.
In Authorised Javascript origins, add http://localhost:portnumber
In Authorised redirect URLs, add http://localhost:portnumber/accounts/google/login/callback/ and http://localhost:portnumber
and save the above changes.

## create a virtual environment and activate it.
<ol>
  <li>python manage.py makemigrations</li>
  <li>python manage.py migrate</li>
  <li>python manage.py runserver portnumber</li>
 </ol>

Temporarily, our machine learning model is demanding a lot of space(>500MB) so we could not host this to a server.
Instead we can use ngrok for temporary.

## Following are the steps
<ol>
  <li>Open a new terminal</li>
  <li>Run the command ngrok http portnumber -host-header="localhost:portnumber"</li>
  <li>A secure tunnel has been created now for safe browsing of your website</li>
  <li>In the new terminal you need to go at http://serveraddress.io to continue further browsing and marking the attendance.</li>
</ol>

## Features
User Friendly, Secured
One tap Login,Logout,Data Update,auto complete search(for easier search),
Hassle Free Attendance within minutes


## Highlights
Following are the steps in our Application.<br>
<ol>
  <li><b>Login Screen</b><br><img  width="50%" src="https://github.com/scarlet2131/ams/blob/master/AMS_ReadMe_Images/AMS_1.png"></li>
  <li><b>Course Page</b><br><img  width="50%" src="https://github.com/scarlet2131/ams/blob/master/AMS_ReadMe_Images/AMS_2.png"></li>
  <li><br><img  width="50%" src="https://github.com/scarlet2131/ams/blob/master/AMS_ReadMe_Images/AMS_3.png"></li>
  <li><b>Attendance Page</b><br><img  width="50%" src="https://github.com/scarlet2131/ams/blob/master/AMS_ReadMe_Images/AMS_4.png"></li>
  <li><b>Image Recognition</b><br><img  width="50%" src="https://github.com/scarlet2131/ams/blob/master/AMS_ReadMe_Images/AMS_5.png"></li>
  <li><b>Recognized ones has been marked</b><br><img  width="50%" src="https://github.com/scarlet2131/ams/blob/master/AMS_ReadMe_Images/AMS_6.png"></li>
  <li><b>Attendance time Up</b><br><img  width="50%" src="https://github.com/scarlet2131/ams/blob/master/AMS_ReadMe_Images/AMS_7.png"></li>
  <li><b>Final Attendance List</b><br><img  width="50%" src="https://github.com/scarlet2131/ams/blob/master/AMS_ReadMe_Images/AMS_8.png"></li>
</ol>
  


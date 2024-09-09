# Django-basic-project
Django basic project for profile

Complete procedure to make a project using Django framework

How to get started with Django projects
First install library
Dir

Pip install Django 
Django-admin startproject  myproject (project- name)

Django-admin --version
Django-

To run Django project
Python manage.py runserver 

If you want to specify port number or IP

Python manage.py runserver 127.0.0.1:9090



We can build multiple tech stacks together like multiple APPs we can install  like 
Website, APIs, Login

Example:
Python manage.py startapp website
Python manage.py startapp apis
Python manage.py startapp login

Make a template folder
Add all your templates like
Profile.html etc

You can set this one and give address of this template in settings.py 
Where
DIR[os.path.templates]


Now make function and call through
Render function

From  django.shortcuts important render 

def home(request):
Print (portfolio function is called from view)
Return render(request, "profile.html",{})

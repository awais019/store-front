from django.core.mail import send_mail, mail_admins, BadHeaderError
from django.shortcuts import render

def say_hello(request):
    try:
        mail_admins('Hello', 'Hello from Awais', html_message='<h1>Hello</h1>')
    except BadHeaderError:
        pass
    return render(request, 'hello.html', { 'name': 'Awais' })
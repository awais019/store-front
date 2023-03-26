from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render

def say_hello(request):
    try:
        message = EmailMessage('subject', 'message', 'fake1@localhost', ['fake2@localhost'])
        message.attach_file('playground/static/images/test.jpeg')
        message.send()
    except BadHeaderError:
        pass
    return render(request, 'hello.html', { 'name': 'Awais' })
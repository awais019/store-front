from django.http import HttpResponse
# Create your views here.


def server_check(request):
    return HttpResponse("Server is up and running!")

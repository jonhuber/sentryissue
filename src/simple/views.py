from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, welcome to the www index.")


def error(request):
    value = 1 / 0
    return HttpResponse("Error, this is an error page.")

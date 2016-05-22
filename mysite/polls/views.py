from django.http import HttpResponse


def index(request):
    return HttpResponse("Quack quack! This is your polls app.")

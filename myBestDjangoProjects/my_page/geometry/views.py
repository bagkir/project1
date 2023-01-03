from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from math import pi
from django.urls import reverse
# Create your views here.


def trainingcss(request):
    return render(request, 'geometry/training.html')


def get_rectangle_area(request, width, height):
    return render(request, 'geometry/rectangle.html')


def get_square_area (request, width):
    return render(request, 'geometry/square.html')


def get_circle_area (request, radius):
    return render(request, 'geometry/circle.htm.html')



def get_rectangle_area_1(request, width, height):
    redirect_url = reverse('rectangle-name', args=(width, height))
    return HttpResponseRedirect(redirect_url)


def get_square_area_1 (request, width):
    redirect_url = reverse('square-name', args=[width])
    return HttpResponseRedirect(redirect_url)


def get_circle_area_1 (request, radius):
    redirect_url = reverse('circle-name', args=[radius])
    return HttpResponseRedirect(redirect_url)

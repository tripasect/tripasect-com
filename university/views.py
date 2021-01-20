import mimetypes
from django.shortcuts import render


def university(request):
    return render(request, 'university/university.html', {'title': 'University'})


def linear_algebra(request):
    return render(request, 'university/linear-algebra/linear-algebra.html', {'title': 'Linear Algebra'})


def advanced_programming(request):
    return render(request, 'university/advanced-programming/advanced-programming.html', {'title': 'Advanced Programming'})


def basic_programming(request):
    return render(request, 'university/basic-programming/basic-programming.html', {'title': 'Basic Programming'})


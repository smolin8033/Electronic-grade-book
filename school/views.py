from django.shortcuts import render
from .models import Student


def test_view(request):
    return render(request, "login.html")


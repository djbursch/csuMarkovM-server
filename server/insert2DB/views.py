from django.shortcuts import render
from django.http import HttpResponse
from .models import Array

def index(request):
    latest_array_list = Array.objects.order_by('-pub_date')[:5]
    output = ', '.join([a.array_num for a in latest_array_list])
    return HttpResponse(output)

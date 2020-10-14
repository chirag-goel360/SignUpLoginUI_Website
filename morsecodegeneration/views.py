from django.http import HttpResponse
from django.shortcuts import render,redirect
def index(request):
    return render(request,'morsecodegeneration/index.html')

def login(request):
    return render(request,'morsecodegeneration/login.html')
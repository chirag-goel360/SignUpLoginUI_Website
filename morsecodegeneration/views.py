from django.shortcuts import render


def index(request):
    return render(request, 'morsecodegeneration/index.html')


def login(request):
    return render(request, 'morsecodegeneration/login.html')


def mainpage(request):
    return render(request, 'morsecodegeneration/mainpage.html')


def contactus(request):
    return render(request, 'morsecodegeneration/contactus.html')


def mouseclick(request):
    return render(request, 'morsecodegeneration/mouseclickevent.html')


def eyeblink(request):
    return render(request, 'morsecodegeneration/eyeblinkevent.html')
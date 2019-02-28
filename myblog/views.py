from django.shortcuts import render, HttpResponse
from . import models


def register(request):
    if request.models == 'GET':
        return render(request, 'myblog/register.html')
    elif request.models == 'POST':
        name = request.POST.get('user')
        password = request.POST.get('password')
        print(name, password)
    return render(request, 'mybolg/regist_success.html')

# Create your views here.

from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.models import User

def LoginFrontView(request):
    if request.user.is_authenticated:
        return redirect(request.GET.get('next') or 'FrontPage')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(request.GET.get('next') or 'FrontPage')
        else:
            error = "Пароль неверный!"
            context = {
                'error': error
            }
            return render(request, 'front/login.html', context)
    return render(request,
                  'front/login.html',
                  {'next': request.GET.get('next') or reverse('FrontPage')})

def logoutFrontView(request):
    logout(request)
    return redirect('front-login')


def RegisterFrontView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['password-1']
        context = {
            'username': username,
        }
        if password == re_password:
            try:
                user = User.objects.get(username=username)
                context['error'] = 1
                return render(request, 'front/login.html', context=context)
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('FrontPage')


        else:
            context['error'] = 2
            return render(request, 'front/login.html', context=context)
    else:
        context = {
        }
    return render(request, 'front/login.html', context=context)


from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model
from django.shortcuts import render, redirect

from django.core.exceptions import ValidationError
from django.core.validators import validate_email


# Create your views here.
def index(request):
    if request.method == 'GET':
        logout = request.GET.get('logout')

        if logout is not None:
            auth_logout(request)
            return redirect('index')

    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Incorrect username or password!'})

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        name = request.POST['name']
        user_type = request.POST['user_type']

        try:
            validate_email(email)
        except ValidationError as e:
            return render(request, 'register.html', {'error': 'Please enter a valid email!'})

        if not username.strip() or not email.strip() or \
                not password.strip() or not confirm_password.strip() or password != confirm_password or \
                not name.strip() or not user_type.strip():

            return render(request, 'register.html', {'error': 'Passwords do not match!'})

        user = get_user_model().objects.create_user(username=username,
                                                    email=email,
                                                    password=password)

        if user is not None:
            user.name = name
            user.user_type = user_type
            user.save()

            auth_login(request, user)
            return redirect('index')

    return render(request, 'register.html')

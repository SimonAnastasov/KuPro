from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model
from django.shortcuts import render, redirect, get_object_or_404

from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from .models import Ad


# Create your views here.
def index(request):
    ads = Ad.objects.all()

    if request.method == 'GET':
        logout = request.GET.get('logout')

        if logout is not None:
            auth_logout(request)
            return redirect('index')

    return render(request, 'index.html', {'user': request.user, 'ads': ads})


def ad_details(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)

    return render(request, 'ad_details.html', {'user': request.user, 'ad': ad})


def my_ads(request):
    ads = Ad.objects.filter(seller_owner=request.user)
    return render(request, 'my_ads.html', {'user': request.user, 'ads': ads})


def add_ad(request):
    if request.method == 'POST':
        title = request.POST["title"]
        description = request.POST["description"]
        price = request.POST["price"]
        image = request.FILES.get("image")

        ad = Ad(title=title, description=description, price=price, image=image, seller_owner=request.user)
        ad.save()

        return redirect('successfully_added_ad')

    return render(request, 'add_ad.html', {})


def successfully_added_ad(request):
    return render(request, 'successfully_added_ad.html', {})


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
        phone = request.POST['phone']

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
            user.phone = phone
            user.save()

            auth_login(request, user)
            return redirect('index')

    return render(request, 'register.html')

"""
URL configuration for KuPro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from KuProApp.views import index, login, register, ad_details, my_ads, add_ad, successfully_added_ad

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='index'),
    path('ad/<int:ad_id>/', ad_details, name='ad_details'),

    path('my_ads/', my_ads, name='my_ads'),
    path('ad/add/', add_ad, name='add_ad'),
    path('ad/add/success', successfully_added_ad, name='successfully_added_ad'),

    path('login/', login, name='login'),
    path('register/', register, name='register'),

    path("__reload__/", include("django_browser_reload.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


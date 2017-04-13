"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from contacts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^contacts/',
        views.contact_list,
        name='contact_list'),

    url(r'^cities/',
        views.city_list,
        name='city_list'),

    url(r'^states/',
        views.state_list,
        name='state_list'),

    url(r'^contact_create/',
        views.contact_create,
        name='contact_create'),

    url(r'^city_create/',
        views.city_create,
        name='city_create'),

    url(r'^state_create/',
        views.state_create,
        name='state_create'),

    url(r'^$',
        views.index,
        name='index'),

]

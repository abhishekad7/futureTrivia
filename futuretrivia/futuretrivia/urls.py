"""futuretrivia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include, re_path
from .import views

urlpatterns = [
	path('', views.index, name='index'),
    path('about/', include('apps.about.urls')),
    path('users/', include('apps.users.urls')),
    path('trivia/', include('apps.trivia.urls')),
    path('practice/', include('apps.practice.urls')),
    path('community/', include('apps.community.urls')),
    path('admin/', admin.site.urls),
    re_path('(?P<url>.+)/$',views.notFound, name="notfound"),
]

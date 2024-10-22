"""
URL configuration for chefstables project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include  #path 는 <str: dish> 와 같이 URL pattern 떄문에 넣음

from myapp import views, urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name = "home"),
    path('homepage/', views.hompage),
    path('display_date/', views.display_date),
    path('home/', views.home),
    path('dishes/<str:dish>', views.menuitems),
    path('myapp/', include(urls))
]
# Change
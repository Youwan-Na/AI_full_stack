from django.urls import path
from myapp import views

urlpatterns = [
    path('home/', views.home),
    path('dishes/<str:dish>',views.menuitems), #dish = pasta
]
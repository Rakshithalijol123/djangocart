from django.urls import path
from . import views

urlpatterns = [
    path('signin/',views.signin),
    path('otp/<str:gmail>/',views.otp),
    path('login/',views.login),
    path('logout/',views.logout),
]
from django.urls import path
from .views import SigninView,SignupView,Sign_out

urlpatterns = [
  path('signin/',SigninView,name='signin'),
  path('signup/',SignupView,name='signup'),
  path('signout/',Sign_out,name='signout'),
]
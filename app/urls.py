from django.urls import path

from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('user_register',views.user_register,name='user_register'),
    path('user_view',views.user_view,name='user_view'),
    path('login',views.login,name='login'),
]
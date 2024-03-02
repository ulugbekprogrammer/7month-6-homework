from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('', views.active, name='active'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]
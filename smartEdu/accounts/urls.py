from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
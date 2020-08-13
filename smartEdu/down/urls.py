
from django.urls import path
from . import views


app_name = 'down'

urlpatterns = [
    path('', views.down, name="down"),
]

#여기서부터작성#


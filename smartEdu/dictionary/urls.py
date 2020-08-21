from django.urls import path
from . import views


app_name = 'dictionary'

urlpatterns = [
    path('', views.showDictionary, name="showDictionary"),
    path('search', views.search, name="search"),
    path('add/<str:user>/<str:dNO>', views.add, name="add"),
    path('mydictionary/<str:user>', views.mydictionary, name="mydictionary"),

]
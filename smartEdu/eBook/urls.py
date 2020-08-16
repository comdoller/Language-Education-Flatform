
from django.urls import path
from . import views


app_name = 'eBook'

urlpatterns = [
    path('', views.eBook, name="eBook"),
    path('viewpdf/<int:NO>/', views.viewpdf, name="viewpdf"),
]
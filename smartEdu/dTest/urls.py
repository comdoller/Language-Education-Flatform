from django.urls import path
from . import views

app_name = 'dTest'

urlpatterns = [
	path('', views.dTest_main, name="dTest_main"),
	path('dTest', views.dTest, name="dTest"),
	path('result', views.result, name='result'),
]
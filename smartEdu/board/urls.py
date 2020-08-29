from django.urls import path, include
from . import views


app_name = 'board'


urlpatterns = [
    path('', views.board, name="board"),
    path('board',views.board),
    path('write',views.write),
    path('insert',views.insert),
    #path('download',views.download),
    path('detail',views.detail),
    path('modify', views.modify, name="modify"),
    path('update',views.update),
    path('delete',views.delete),
    path('reply_insert',views.reply_insert),
    path('list',views.list, name="list"),
]

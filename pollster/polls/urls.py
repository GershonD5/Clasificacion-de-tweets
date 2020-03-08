from django.urls import path

from . import views

app_name='polls'
urlpatterns =[ 
    path('', views.index,name='index'),
    path('<int:tweet_id>/',views.detail, name='detail'),
    path('<int:tweet_id>/results/',views.results, name='results'),
    path('<int:tweet_id>/ofensivo/',views.ofensivo, name='ofensivo'),
    path('<int:tweet_id>/NoOfensivo/',views.NoOfensivo, name='NoOfensivo'),
    path('votar',views.votar, name='votar')

    

]
from django.conf.urls import url
from django.urls import path
from main_app import views

urlpatterns = [
    url(r'^movies/', views.MovieView.as_view(), name='movies'),
    url(r'^comments/$', views.CommentView.as_view(), name='comments'),
    url(r'^comments/(?P<pk>\d+)/', views.CommentView.as_view(), name='comments'),
    url(r'^top/(?P<start_time>[\w\-\.]+)/(?P<end_time>[\w\-\.]+)/$', views.MovieRankingView.as_view(), name='ranking'),
    url(r'^top/$', views.MovieRankingView.as_view(), name='ranking')
]

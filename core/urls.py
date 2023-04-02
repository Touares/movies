from django.urls import path, include
from . import views

urlpatterns = [
     path('genre_get_post', views.GenreGetPost.as_view(), name='genre_get_post'),
     path('movie_get_post', views.MovieGetPost.as_view(), name='movie_get_post'),
     path('genre_pk/<str:pk>', views.GenrePk.as_view(), name='genre_pk'),
     path('movie_pk/<str:pk>', views.MoviePk.as_view(), name='movie_pk'),
]
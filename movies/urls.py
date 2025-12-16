from django.urls import path
from .views import MovieListCreateAPIView, MovieDetailAPIView

urlpatterns = [
    path('', MovieListCreateAPIView.as_view()),
    path('<int:pk>', MovieDetailAPIView.as_view()),
]

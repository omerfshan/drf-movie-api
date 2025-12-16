from django.urls import path
from .views import MovieListAPIView, MovieDetailAPIView

urlpatterns = [
    path('', MovieListAPIView.as_view()),
    path('<int:pk>', MovieDetailAPIView.as_view()),
]

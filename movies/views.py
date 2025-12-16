from rest_framework import generics

from .models import Movies
from .Serializers import (
    MovieSerializer,
    MovieDetails,
    MovieCreateSerializer,
    MovieUpdateSerializer
)


class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movies.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return MovieCreateSerializer
        return MovieSerializer


class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieDetails
        return MovieUpdateSerializer

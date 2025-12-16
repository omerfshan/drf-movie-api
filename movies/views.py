from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Movies
from .Serializers import (
    MovieSerializer,
    MovieDetails,
    MovieCreateSerializer,
    MovieUpdateSerializer
)


class MovieListAPIView(APIView):

    def get(self, request):
        movies = Movies.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MovieCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Movies.objects.get(pk=pk)
        except Movies.DoesNotExist:
            return None

    def get(self, request, pk):
        movie = self.get_object(pk)
        if not movie:
            return Response(
                {"detail": "Film bulunamadı."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = MovieDetails(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        movie = self.get_object(pk)
        if not movie:
            return Response(
                {"detail": "Film bulunamadı."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = MovieUpdateSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        movie = self.get_object(pk)
        if not movie:
            return Response(
                {"detail": "Film bulunamadı."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = MovieUpdateSerializer(
            movie, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie = self.get_object(pk)
        if not movie:
            return Response(
                {"detail": "Film bulunamadı."},
                status=status.HTTP_404_NOT_FOUND
            )
        movie.delete()
        return Response(
            {"detail": "Film başarıyla silindi."},
            status=status.HTTP_204_NO_CONTENT
        )

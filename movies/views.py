from rest_framework import generics
from drf_spectacular.utils import extend_schema, extend_schema_view

from .models import Movies
from .Serializers import (
    MovieSerializer,
    MovieDetails,
    MovieCreateSerializer,
    MovieUpdateSerializer
)


@extend_schema_view(
    get=extend_schema(
        summary="Film Listesi",
        description="Sistemdeki tüm filmleri listeler.",
        responses=MovieSerializer(many=True),
    ),
    post=extend_schema(
        summary="Film Oluştur",
        description="Yeni bir film kaydı oluşturur.",
        request=MovieCreateSerializer,
        responses={201: MovieCreateSerializer},
    ),
)
class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movies.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return MovieCreateSerializer
        return MovieSerializer


@extend_schema_view(
    get=extend_schema(
        summary="Film Detayı",
        description="ID ile tek bir filmin detaylarını getirir.",
        responses=MovieDetails,
    ),
    put=extend_schema(
        summary="Film Güncelle (PUT)",
        description="Filmin tüm alanlarını günceller.",
        request=MovieUpdateSerializer,
        responses=MovieUpdateSerializer,
    ),
    patch=extend_schema(
        summary="Film Güncelle (PATCH)",
        description="Filmin belirli alanlarını günceller.",
        request=MovieUpdateSerializer,
        responses=MovieUpdateSerializer,
    ),
    delete=extend_schema(
        summary="Film Sil",
        description="Filmi sistemden siler.",
        responses={204: None},
    ),
)
class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieDetails
        return MovieUpdateSerializer

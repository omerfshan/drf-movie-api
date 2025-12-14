
from django.shortcuts import render
from .models import Movies
from .Serializers import MovieDetails,MovieSerializer,MovieCreateSerializer

from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def movie_list(request):
    if(request.method=='GET'):
        movies = Movies.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    elif(request.method=="POST"):
        serializer=MovieCreateSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def movie_detail(request, pk):
    movie = Movies.objects.get(pk=pk)
    serializer = MovieDetails(movie)
    return Response(serializer.data)  

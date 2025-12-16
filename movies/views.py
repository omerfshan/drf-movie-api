
from django.shortcuts import render
from .models import Movies
from .Serializers import MovieDetails,MovieSerializer,MovieCreateSerializer,MovieUpdateSerializer

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

@api_view(['GET','PUT','PATCH','DELETE'])
def movie_detail(request, pk):
    try:
        movie=Movies.objects.get(pk=pk)
    except Movies.DoesNotExist:
        return Response({'detail':'film bulunamadi.'},status=status.HTTP_404_NOT_FOUND)
    
    if(request.method=='GET'):
        serializer = MovieDetails(movie)
        return Response(serializer.data)
    elif request.method in ['PUT','PATCH']:
        partial=request.method=='PATCH'
        serializer=MovieUpdateSerializer(movie,data=request.data,partial=partial)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        movie.delete()
        return Response({'details: Film başarıyla silindi.'},status=status.HTTP_204_NO_CONTENT)
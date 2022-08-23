from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import MovieSerializer, MovieDetailSerializer, DirectorSerializer, ReviewSerializer
from movie_app.models import Director, Movie, Review

# Create your views here.


@api_view(["GET"])
def directors_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
def director_view(request, id):
    try:
       director = Director.objects.get(id=id)
    except:
        return Response(data={'error': 'Director not found'}, status=404)
    serializer = DirectorSerializer(director)
    return Response(data=serializer.data)


@api_view(["GET"])
def movie_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
def movie_detail_view(request, id):
    try:
       movie = Movie.objects.get(id=id)
    except:
        return Response(data={'error': 'Movie not found'}, status=404)
    serializer = MovieDetailSerializer(movie)
    return Response(data=serializer.data)


@api_view(["GET"])
def review_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data)


@api_view(["GET"])
def review_item_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except:
        return Response(data={'error': 'Review not found'}, status=404)
    serializer = ReviewSerializer(review)
    return Response(data=serializer.data)


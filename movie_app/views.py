from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Director, Movie, Review
from movie_app.serializers import DirectorSerializer, DirectorDetailSerializer, MovieSerializer, MovieDetailSerializer, \
    ReviewSerializer


@api_view(['GET'])
def director_details(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found!'},
            status=status.HTTP_404_NOT_FOUND)

    data = DirectorDetailSerializer(director).data
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def director_list(request):
    directors = Director.objects.all()

    serializer = DirectorSerializer(directors, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_list(request):
    movie = Movie.objects.all()

    serializer = MovieSerializer(movie, many=True).data

    return Response(data=serializer, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_details(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found!'}
                        ,status=status.HTTP_404_NOT_FOUND)

    serializer = MovieDetailSerializer(movie).data

    return Response(data=serializer, status=status.HTTP_200_OK)

@api_view(['GET'])
def review_list(request):
    review = Review.objects.all()

    serializer = ReviewSerializer(review, many=True).data

    return Response(data=serializer, status=status.HTTP_200_OK)

@api_view(['GET'])
def review_details(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found!'},
                        status=status.HTTP_404_NOT_FOUND)

    serializer = ReviewSerializer(review).data

    return Response(data=serializer, status=status.HTTP_200_OK)




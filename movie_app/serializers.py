from rest_framework import serializers
from .models import Movie, Director, Review

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name'.split()

class DirectorDetailSerializer(DirectorSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title director'.split()

class MovieDetailSerializer(MovieSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'movie'.split()



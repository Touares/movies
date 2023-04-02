from rest_framework import serializers
from .models import (Genre, Movie)
from rest_framework import status, filters
from rest_framework.response import Response

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class MovieSerializer(serializers.ModelSerializer):

    # genre = GenreSerializer()
    genre = serializers.SlugRelatedField( queryset=Genre.objects.all(),
        
        slug_field='id',
    )

    class Meta:
        model = Movie
        fields = ['id', 'genre', 'title', 'numberInStock', 'dailyRentalRate',
                  'publishDate', 'liked']
        depth=1

    # def create(self, validated_data):
    #     # Get the genre ID from the validated data
    #     genre_id = validated_data.pop('genre')

    #     # Get the genre object with the specified primary key
    #     try:
    #         genre = Genre.objects.get(id=genre_id)
    #     except Genre.DoesNotExist:
    #         raise serializers.ValidationError('Invalid genre ID')

    #     # Create and save the movie object with the retrieved genre
    #     movie = Movie.objects.create(genre=genre, **validated_data)

    #     return movie
    
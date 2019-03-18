from main_app.models import Movie, Comment, Rating
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment_text', 'movie_id', 'posted_date')


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('movie_id','source', 'value')
        extra_kwargs = {"movie_id": {"write_only": True}}

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class RankSerializer(serializers.Serializer):
    movie_id = serializers.IntegerField()
    total_comments = serializers.IntegerField()
    rank = serializers.IntegerField()

from django.shortcuts import render
import requests
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
import re
from main_app.serializers import (MovieSerializer, RatingSerializer,
                                            CommentSerializer, RankSerializer)
from main_app.models import Movie, Rating, Comment
from django.db.models import Count


class MovieView(APIView):

    def convert(self, name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def get(self, request):
        movies = Movie.objects.all()
        response_data = []
        for movie in movies:
            ratings = Rating.objects.filter(movie_id=movie.id)
            rating_serializer = RatingSerializer(ratings, many=True)
            movie_serializer = MovieSerializer(movie)
            data = movie_serializer.data
            data['ratings'] = rating_serializer.data
            response_data.append(data)

        return Response({"movies":response_data})

    def post(self, request):
        if request.data.get('title'):
            results = requests.get('http://www.omdbapi.com/?t=' + request.data.get('title') + '&apikey=13696f4c')
            data = results.json()
            data_movies = {}
            data_ratings = []
            for key in data:
                data_movies[self.convert(key)] = data[key]
                if key == "Ratings":
                    for rate in data[key]:
                        temp_rate = {}
                        for rate_key in rate:
                            temp_rate[self.convert(rate_key)] = rate[rate_key]
                        data_ratings.append(temp_rate)

            movie_serializer = MovieSerializer(data=data_movies)
            if movie_serializer.is_valid():
                movie_serializer.save()
            movie = Movie.objects.get(title=data_movies['title'])
            for rate in data_ratings:
                rate['movie_id'] = movie.id
            rating_serializer = RatingSerializer(data=data_ratings, many=True)
            if rating_serializer.is_valid():
                rating_serializer.save()
                return Response(data)

            return Response(movie_serializer.errors)

        return Response("Please provide title of the movie")


class CommentView(APIView):

    def get(self, request, pk=None):
        if pk:
            comment = Comment.objects.filter(movie_id=pk)
            comment_serializer = CommentSerializer(comment, many=True)
        else:
            comments = Comment.objects.all()
            comment_serializer = CommentSerializer(comments, many=True)
        return Response({'comments': comment_serializer.data})


    def post(self, request):
        comment = {}
        comment['movie_id'] = request.data.get('id')
        comment['comment_text'] = request.data.get('comment')
        comment_serializer = CommentSerializer(data=comment)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response(comment_serializer.data)
        return Response(comment_serializer.errors)


class MovieRankingView(APIView):

    def get(self, request, start_time=None, end_time=None):
        if start_time != None and end_time != None:

            comments = Comment.objects.filter(posted_date__range=[start_time, end_time]).values('movie_id').annotate(total_comments=Count('movie_id'))
            comments_list = sorted(list(comments), key=lambda k: k['total_comments'])
            rank = 1
            comments_list[len(comments_list) - 1]['rank'] = rank
            for index in reversed(range(1, len(comments_list))):
                if comments_list[index]['total_comments'] != comments_list[index - 1]['total_comments']:
                    rank += 1
                comments_list[index - 1]['rank'] = rank
            rank_serializer = RankSerializer(comments_list, many=True)

            return Response(rank_serializer.data)

        return Response("Please specify date range")

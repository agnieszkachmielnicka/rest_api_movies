from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=500)
    year = models.CharField(max_length=10)
    rated = models.CharField(max_length=10)
    released = models.CharField(max_length=500)
    genre = models.CharField(max_length=500)
    director = models.CharField(max_length=500)
    writer = models.CharField(max_length=500)
    actors = models.CharField(max_length=500)
    plot = models.TextField(max_length=1000)
    language = models.CharField(max_length=500)
    country = models.CharField(max_length=500)
    awards = models.CharField(max_length=500)
    poster = models.URLField()
    metascore = models.CharField(max_length=10)
    imdb_rating = models.CharField(max_length=10)
    imdb_votes = models.CharField(max_length=100)
    imdb_id = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    dvd = models.CharField(max_length=100)
    box_office = models.CharField(max_length=100)
    production = models.CharField(max_length=100)
    website = models.CharField(max_length=500)


class Comment(models.Model):
    comment_text = models.TextField(max_length=500)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    posted_date = models.DateField(auto_now_add=True)


class Rating(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    source = models.CharField(max_length=500)
    value = models.CharField(max_length=100)

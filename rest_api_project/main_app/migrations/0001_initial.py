# Generated by Django 2.1.7 on 2019-03-18 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(max_length=500)),
                ('posted_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('year', models.CharField(max_length=10)),
                ('rated', models.CharField(max_length=10)),
                ('released', models.CharField(max_length=500)),
                ('genre', models.CharField(max_length=500)),
                ('director', models.CharField(max_length=500)),
                ('writer', models.CharField(max_length=500)),
                ('actors', models.CharField(max_length=500)),
                ('plot', models.TextField(max_length=1000)),
                ('language', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=500)),
                ('awards', models.CharField(max_length=500)),
                ('poster', models.URLField()),
                ('metascore', models.CharField(max_length=10)),
                ('imdb_rating', models.CharField(max_length=10)),
                ('imdb_votes', models.CharField(max_length=100)),
                ('imdb_id', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('dvd', models.CharField(max_length=100)),
                ('box_office', models.CharField(max_length=100)),
                ('production', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=500)),
                ('value', models.CharField(max_length=100)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Movie')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='movie_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Movie'),
        ),
    ]

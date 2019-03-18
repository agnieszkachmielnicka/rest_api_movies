###### HEROKU URL #######
https://chmielnickarestapi.herokuapp.com

##### POST MOVIES #### -> getting movie by title from http://www.omdbapi.com/ and saving to database
/movies/

example request body:
{
  "title" : "Star Wars"
}

#### GET MOVIES ##### -> getting all list presented in database
/movies/

#### GET COMMENTS #####
/comments/ -> getting all presented comments
/comments/2/ -> getting comments for movie with id 2

#### POST COMMENTS #### -> adding comment to movie with id 3
/comments/

example request body:
{
  "id" : "3",
  "comment": "this is comment"
}

### GET TOP #### -> getting ranking of the movies with comments added in specific data range
/top/2019-03-01/2019-03-19

# import app variable from init file from the app directory
from app import app
from movie_recommender import *

from flask import render_template, request

# this function runs when a person enters this URL on the website
# render_template will render the site in the html format specified by the index.html file
@app.route("/", methods = ["GET", "POST"])
def index():

    if request.method == "POST":
        req = request.form
        movie = req.get("Movie")
        sorted_movies = recommend_movie(movie)
        return render_template("results.html", movie = movie, sorted_movies = sorted_movies, get_title_from_index = get_title_from_index)

    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")
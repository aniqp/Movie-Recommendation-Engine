## Content-based movie recommendation engine implementing a cosine similarity algorithm with NumPy and Pandas (ML & NLP - TFIDVectorizer)
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

## Step 1: Read CSV File
df = pd.read_csv("movie_dataset.csv")
### helper functions - get value with values[0] instead of table ###

def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title.str.lower() == title.lower()]["index"].values[0]

def recommend_movie(movie):

	## Step 2: Select Features

	features = ['keywords', 'cast', 'genres', 'director']

	## Step 3: Create a column in DF which combines all selected features

	# Replace missing keyword values with empty strings
	for feature in features:
		df[feature] = df[feature].fillna('')

	def combine_features(df_row):
		return df_row['keywords'] + " " + df_row['genres']

	df["combined_features"] = df.apply(combine_features, axis = 1)

	## Step 4: Create count matrix from this new combined column

	cv = CountVectorizer()

	# this transforms the text in the entire column into a vector on the basis of the frequency (count) of each word that occurs in the entire text
	count_matrix = cv.fit_transform(df["combined_features"])

	## Step 5: Compute the Cosine Similarity based on the count_matrix
	cosine_sim = cosine_similarity(count_matrix)

	if movie == "":
		return "No movie title was entered. Please enter a movie title."

	## Step 6: Get index of this movie from its title
	try:
		movie_index = get_index_from_title(movie)
		## Obtain list of tuples, assigning indices to cosine similarities
		similar_movies = list(enumerate(cosine_sim[movie_index]))

		## Step 7: Get a list of similar movies in descending order of similarity score

		# Sorting based on second element of each tuple (cosine similarity value, in descending order)
		sorted_similar_movies = sorted(similar_movies, key = lambda x:x[1], reverse = True)
		sorted_similar_movies = sorted_similar_movies[1:51]

		## Step 8: Print titles of first 50 movies

		return sorted_similar_movies
	except:
		return "Sorry, this movie isn't in our database. Please check that you've spelled the movie correctly or enter another movie title."



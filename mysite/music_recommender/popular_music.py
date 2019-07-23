import pandas
from sklearn.model_selection import train_test_split
from music_recommender.popularity import popularity
import os

def get_popular_music(user_id, path):
	song_df = pandas.read_csv("final.csv")
	users = song_df['user_id'].unique()
	songs = song_df['song'].unique()
	train_data, test_data = train_test_split(song_df, test_size = 0.20, random_state=0)
	user = users[user_id]
	p = popularity()
	p.create(train_data, 'user_id', 'song')
	rec = p.recommend(user)
	pandas.set_option('display.max_rows', 500)
	pandas.set_option('display.max_columns', 500)
	pandas.set_option('display.width', 2000)
	popular_songs = []
	with pandas.option_context('display.max_rows', None, 'display.max_columns', None):
		list_of_songs = rec['song'].to_string(index=False).split("\n")
	for song in list_of_songs:
		popular_songs.append(song.strip())
	return popular_songs
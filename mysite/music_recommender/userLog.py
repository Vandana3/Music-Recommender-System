import pandas

def get_user_items(user_id, path):
	song_df = pandas.read_csv("final.csv")
	users = song_df['user_id'].unique()
	user = users[int(user_id)]
	songs = []
	input2= song_df[song_df['user_id'] == user].index.tolist()
	for i in range(len(input2)):
		song=song_df['song'][input2[i]]
		songs.append(song)
	return songs
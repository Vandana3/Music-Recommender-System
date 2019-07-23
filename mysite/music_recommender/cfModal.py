import numpy as np
import pandas 
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import cosine, correlation

def cf_itembased(user_id,path):
	song_df4 = pandas.read_csv("final.csv")

	users = song_df4['user_id'].unique()
	songs = song_df4['song_id'].unique()

	song_df5= pandas.DataFrame()
	song_df5['song_id']=song_df4['song_id']
	song_df5['song']=song_df4['song']
	song_df5.index=song_df4.index
	song_df5 = song_df5.drop_duplicates()



#Creating a pivot table with the following parameters
	count_matrix = song_df4.pivot_table(index=['song_id'],columns=['user_id'],values='listen_count').reset_index(drop=True)
	count_matrix.fillna( 0, inplace = True )

#Calculating Cosine Similiarities
	song_similarity = 1 - pairwise_distances( count_matrix.as_matrix(), metric="cosine" )

#Filling diagonals with 0s instead of 1 to avoid recommending the same song when sorting
	np.fill_diagonal( song_similarity, 0 )
	count_matrix = pandas.DataFrame( song_similarity )
	similar_songs={}



	try:
		user= users[user_id]
    		#print("Recommendations for user ", user)
		input2= song_df4[song_df4['user_id'] == user].index.tolist()
		for i in range(len(input2)):
			key=song_df4['song'][input2[i]]
			song= song_df4['song_id'][input2[i]]
			#print("Recommended songs based on song id - ", song ," and song -  ",song)

			inp = song_df4[song_df4['song_id'] == song].index.tolist()
			inp = inp[0]
			song_df5['similarity'] = count_matrix.iloc[inp]
			song_df5.columns = ['song_id', 'song','similarity']
			similar_songs[key]=[]
			if (song_df4['listen_count'][input2[i]] <= 2) & (song_df4['listen_count'][input2[i]]>=1):
				with pandas.option_context('display.max_rows', None, 'display.max_columns', None):
					similar_songs[key].append(song_df5.sort_values(["similarity"], ascending=False)['song'][0:2].to_string(index=False).strip())
				#print(song_df5.sort_values(["similarity"], ascending=False)['song'][0:2])
			elif song_df4['listen_count'][input2[i]]< 5:
				with pandas.option_context('display.max_rows', None, 'display.max_columns', None):
					similar_songs[key].append(song_df5.sort_values(["similarity"], ascending=False)['song'][0:5].to_string(index=False).strip())
				#print(song_df5.sort_values(["similarity"], ascending=False)['song'][0:5])
			elif song_df4['listen_count'][input2[i]]< 10:
				with pandas.option_context('display.max_rows', None, 'display.max_columns', None):
					similar_songs[key].append(song_df5.sort_values(["similarity"], ascending=False)['song'][0:10].to_string(index=False).strip())
				#print(song_df5.sort_values(["similarity"], ascending=False)['song'][0:10])
			elif song_df4['listen_count'][input2[i]]> 10:
				with pandas.option_context('display.max_rows', None, 'display.max_columns', None):
					similar_songs[key].append(song_df5.sort_values(["similarity"], ascending=False)['song'][0:10].to_string(index=False).strip())
				#print(song_df5.sort_values(["similarity"], ascending=False)['song'][0:10])
                
	except:
		print("Sorry, the user id is not in the database!")

	return similar_songs


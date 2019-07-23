import numpy as np
import pandas
def genreRecommend(user_id,path1,path2):
	df1 = pandas.read_csv("final.csv")
	df2 = pandas.read_csv("datafinal.csv",encoding = 'unicode_escape')
	users = df1['user_id'].unique()
	songs = df1['song_id'].unique()

	rock={}
	blues={}
	country={}
	metal={}
	classical={}
	jazz={}
	disco={}
	reggae={}
	hiphop={}
	pop={}
   
	for i in range(len(df2)):
		if df2['genre'][i]== "rock":
			songID=df2['song_id'][i]
			songTitle=df2['title'][i]
			rock[songID]=songTitle
        
		elif df2['genre'][i]=="blues":
			songID=df2['song_id'][i]
			songTitle=df2['title'][i]
			blues[songID]=songTitle

        
        
        
		elif df2['genre'][i]=="country":
			songID=df2['song_id'][i]
			songTitle=df2['title'][i]
			country[songID]=songTitle
		        
		        
        
		elif df2['genre'][i]=="metal":
			songID=df2['song_id'][i]
			songTitle=df2['title'][i]
			metal[songID]=songTitle
	        
	        	
        
		elif df2['genre'][i]=="classical":
			songID=df2['song_id'][i]
			songTitle=df2['title'][i]
			classical[songID]=songTitle
        
		elif df2['genre'][i]=="jazz":
			songID=df2['song_id'][i]
			songTitle=df2['title'][i]
			jazz[songID]=songTitle
        
		elif df2['genre'][i]=="disco":
			songID=df2['song_id'][i]
			songTitle=df2['title'][i]        
			disco[songID]=songTitle
        
		elif df2['genre'][i]=="reggae":
			songID=df2['song_id'][i]
			songTitle=df2['title'][i]
			reggae[songID]=songTitle
        
		elif df2['genre'][i]=="hiphop":
			songID=df2['song_id'][i]
			songTitle=df2['title'][i]
			hiphop[songID]=songTitle
        
		elif df2['genre'][i]=="pop":
			songID=df2['song_id'][i]
			songTitle=df2['title'][i]
			pop[songID]=songTitle
        
	similar_genre={}        

	try:
		user= users[user_id]
		input1= df1[df1['user_id'] == user].index.tolist()
		for i in range(len(input1)):
			songID=df1['song_id'][input1[i]]
			songName=df1['song'][input1[i]]
			songGenre=df1['genre'][input1[i]]
			songCount=df1['listen_count'][input1[i]]
			key = songName + ";" + songGenre
			similar_genre[key]=[]

       
			if songCount< 2:
          
				if songGenre=="dance and electronica":
					similar_genre[key].append(list(disco.items())[0:2])
				elif songGenre=="classic pop and rock":
					similar_genre[key].append(list(rock.items())[0:2])
				elif songGenre=="folk":
					similar_genre[key].append(list(country.items())[0:2])
				elif songGenre=="punk":
					similar_genre[key].append(list(rock.items())[0:2])
				elif songGenre=="soul and reggae":
					similar_genre[key].append(list(reggae.items())[0:2])
				elif songGenre=="jazz and blues":
					similar_genre[key].append(list(jazz.items())[0:1])
					similar_genre[key].append(list(blues.items())[0:1])
				elif songGenre=="classical":
					similar_genre[key].append(list(classical.items())[0:2])
				elif songGenre=="pop":
					similar_genre[key].append(list(pop.items())[0:2])
				elif songGenre=="hip-hop":
					similar_genre[key].append(list(hiphop.items())[0:2])
				elif songGenre=="metal":
					similar_genre[key].append(list(metal.items())[0:2])

               
			elif songCount<5:
          
				if songGenre=="dance and electronica":
					similar_genre[key].append(list(disco.items())[0:5])
				elif songGenre=="classic pop and rock":
					similar_genre[key].append(list(rock.items())[0:5])
				elif songGenre=="folk":
					similar_genre[key].append(list(country.items())[0:5])
				elif songGenre=="punk":
					similar_genre[key].append(list(rock.items())[0:5])
				elif songGenre=="soul and reggae":
					similar_genre[key].append(list(reggae.items())[0:5])
				elif songGenre=="jazz and blues":
					similar_genre[key].append(list(jazz.items())[0:2])
					similar_genre[key].append(list(blues.items())[0:2])
				elif songGenre=="classical":
					similar_genre[key].append(list(classical.items())[0:5])
				elif songGenre=="pop":
					similar_genre[key].append(list(pop.items())[0:5])
				elif songGenre=="hip-hop":
					similar_genre[key].append(list(hiphop.items())[0:5])
				elif songGenre=="metal":
					similar_genre[key].append(list(metal.items())[0:5])
                
			else:
          
				if songGenre=="dance and electronica":
					similar_genre[key].append(list(disco.items())[0:10])
				elif songGenre=="classic pop and rock":
					similar_genre[key].append(list(rock.items())[0:10])
				elif songGenre=="folk":
					similar_genre[key].append(list(country.items())[0:10])
				elif songGenre=="punk":
					similar_genre[key].append(list(rock.items())[0:10])
				elif songGenre=="soul and reggae":
					similar_genre[key].append(list(reggae.items())[0:10])
				elif songGenre=="jazz and blues":
					similar_genre[key].append(list(jazz.items())[0:5])
					similar_genre[key].append(list(blues.items())[0:5])
				elif songGenre=="classical":
					similar_genre[key].append(list(classical.items())[0:10])
				elif songGenre=="pop":
					similar_genre[key].append(list(pop.items())[0:10])
				elif songGenre=="hip-hop":
					similar_genre[key].append(list(hiphop.items())[0:10])
				elif songGenre=="metal":
					similar_genre[key].append(list(metal.items())[0:10])

	except:
		print("Sorry, the user id is not in the database!")

	return similar_genre

from django.shortcuts import render
import os
import random
# Create your views here.
from django.http import HttpResponse
from django.conf import settings
from music_recommender.popular_music import *
from music_recommender.userLog import get_user_items
from music_recommender.cfModal import cf_itembased
from music_recommender.genreModal import genreRecommend

# Create your views here.

def home(request):
	#passing to a template
	return render(request, 'music_recommender/index.html')

def popular_music(request, user_id):
	content = dict()
	path = os.path.join(settings.BASE_DIR, 'final.csv')
	content['songs'] = get_popular_music(user_id,path)
	content['songs'] = formatted_songs(content['songs'])
	#passing to a templates
	return render(request, 'music_recommender/popular_songs.html', content)

def cf(request, user_id):
	content = dict()
	path = os.path.join(settings.BASE_DIR, 'final.csv')
	content['songs'] = cf_itembased(user_id,path)
	content['songs'] = format_cf_songs(content['songs'])
	return render(request, 'music_recommender/cf.html', content)

def genre(request, user_id):
	content = dict()
	path1 = os.path.join(settings.BASE_DIR, 'final.csv')
	path2 = os.path.join(settings.BASE_DIR, 'datafinal.csv')
	content['songs'] = genreRecommend(user_id,path1,path2)
	content['songs'] = format_genre_songs(content['songs'])
	return render(request, 'music_recommender/genre.html', content)

def login(request):
	if request.POST:
		user = get_user(request)
		content = dict()
		content['user'] = user
		if not is_valid_user(user):
			content['message'] = 'Login Incorrect'
			return render(request, 'music_recommender/index.html', content)
		if is_new_user(user):
			return render(request, 'music_recommender/new_user_home.html', content)
		content['songs'] = get_user_songs(user)
		return render(request, 'music_recommender/user_home.html', content)
	return render(request, 'music_recommender/index.html')

def signup(request):
	if request.POST:
		user = insert_new_user_to_file(request)
		content = dict()
		content['user'] = user
		return render(request, 'music_recommender/new_user_home.html', content)
	return render(request, 'music_recommender/index.html')

def insert_new_user_to_file(request):
	fullname = request.POST['fullname'].strip()
	username = request.POST['registerusername'].strip()
	password = request.POST['registerpassword'].strip()
	email = request.POST['registeremail'].strip()
	user_id = str(random.randint(999,9999))
	existing_user_ids = set()
	f = open("auth.txt", "r")
	for line in f:
		existing_user_ids.add(line.split(',')[0])
	f.close()
	for x in range(500):
		if user_id not in existing_user_ids:
			break
		user_id = str(random.randint(999,9999))
	line = user_id+","+fullname+","+username+","+email+","+password+"\n"
	user = dict()
	user['user_id'] = user_id
	user['fullname'] = fullname
	user['username'] = username
	user['email'] = email
	user['password'] = password
	f = open("auth.txt", "a")
	f.write(line)
	f.close()
	return user

def get_user(request):
	user = dict()
	f = open("auth.txt", "r")
	for line in f:
		user_info = line.split(',')
		if user_info[2].strip() == request.POST['loginusername'] and user_info[4].strip() == request.POST['loginpassword']:
			user['user_id'] = user_info[0].strip()
			user['fullname'] = user_info[1].strip()
			user['username'] = user_info[2].strip()
			user['email'] = user_info[3].strip()
			user['password'] = user_info[4].strip()
			break
	f.close()
	return user

def is_valid_user(user):
	if user:
		return True
	return False

def is_new_user(user):
	cf_users = set()
	f = open("cf_users.txt", "r")
	for line in f:
		cf_users.add(line.strip())
	f.close()
	if user['user_id'] not in cf_users:
		return True
	return False

def get_user_songs(user):
	user_id = user['user_id']
	path = os.path.join(settings.BASE_DIR, 'final.csv')
	list_of_songs = get_user_items(user_id,path)
	return formatted_songs(list_of_songs)

def formatted_songs(list_of_songs):
	formatted_items = []
	for song in list_of_songs:
		item = dict()
		song_artist = song.split('-')
		if len(song_artist) == 2:
			item['song'] = song_artist[0].strip()
			item['artist'] = song_artist[1].strip()
		elif len(song_artist) == 1:
			item['song'] = song_artist[0].strip()
			item['artist'] = "NA"
		formatted_items.append(item)
	return formatted_items

def format_cf_songs(songs):
	formatted_items = []
	for user_song, rec_songs in songs.items():
		item = dict()
		song_artist = user_song.split('-')
		if len(song_artist) == 2:
			item['song'] = song_artist[0].strip()
			item['artist'] = song_artist[1].strip()
		elif len(song_artist) == 1:
			item['song'] = song_artist[0].strip()
			item['artist'] = "NA"
		if len(rec_songs) == 1:
			rec_song_list = rec_songs[0].split('\n')
			item['recommendations'] = []
			for rec_song in rec_song_list:
				rec_item = dict()
				rec_song_artist = rec_song.split('-')
				if len(rec_song_artist) == 2:
					rec_item['rec_song'] = rec_song_artist[0].strip()
					rec_item['rec_artist'] = rec_song_artist[1].strip()
					item['recommendations'].append(rec_item)
				elif len(rec_song_artist) == 1:
					rec_item['rec_song'] = rec_song_artist[0].strip()
					rec_item['rec_artist'] = "NA"
					item['recommendations'].append(rec_item)
		formatted_items.append(item)
	return formatted_items

def format_genre_songs(songs):
	formatted_items = []
	for user_song, rec_songs in songs.items():
		item = dict()
		song_genre = user_song.split(';')
		if len(song_genre) == 2:
			song_artist = song_genre[0].strip().split('-')
			item['genre'] = song_genre[1].strip()
			if len(song_artist) == 2:
				item['song'] = song_artist[0].strip()
				item['artist'] = song_artist[1].strip()
			elif len(song_artist) == 1:
				item['song'] = song_artist[0].strip()
				item['artist'] = "NA"
		item['recommendations'] = []
		if len(rec_songs) == 1:
			for rec_song in rec_songs[0]:
				if len(rec_song) == 2:
					item['recommendations'].append(rec_song[1])
			formatted_items.append(item)
	return formatted_items


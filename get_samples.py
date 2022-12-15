import requests
import json
import random
import re
from bs4 import BeautifulSoup

all_items = []

for sample_num in range(0,20000):


	user_agents_list = [
 	   'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
 	   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
 	   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
	]

	url = f'https://www.whosampled.com/sample/{sample_num}'

	r = requests.get(url, headers={'User-Agent': random.choice(user_agents_list)})

	if r.status_code == 200:
		print('Sample URL:', url)

		track_artist = None
		sampled_artist = None
		track_name = None
		sample_name = None
	
	# elif r.status_code == 404:
	# 	print("There's no sample here:", url)

		soup = BeautifulSoup(r.text, features="html.parser")

		# GET INFO FOR BOTH ARTISTS
		artist_info = soup.find_all("div",{'class': 'sampleTrackArtists'})

		if len(artist_info) == 2:
			track_artist = artist_info[0]
			sampled_artist = artist_info[1]

			track_artist = track_artist.find('meta', {'itemprop': 'name'})
			track_artist = str(track_artist)[15:-19]

			sampled_artist = sampled_artist.find('meta', {'itemprop': 'name'})
			sampled_artist = str(sampled_artist)[15:-19]

			# print(f'Track Artist: {track_artist}')
			# print(f'Sampled Artist: {sampled_artist}')

		# GET INFO FOR BOTH SONGS
		song_info = soup.find_all("div",{'class': 'sampleTrackInfo'})

		if len(song_info) == 2:
			track_name = song_info[0]
			sample_name = song_info[1]

			track_name = track_name.find('a', {'class': "trackName"})
			
			text1 = str(track_name)
			pattern = re.compile(r'"name">(.+)</span')
			results = pattern.search(text1)
			track_name = results.group(0)[7:-6]

			sample_name = sample_name.find('a', {'class': "trackName"})

			text2 = str(sample_name)
			pattern2 = re.compile(r'"name">(.+)</span')
			results2 = pattern2.search(text2)
			sample_name = results2.group(0)[7:-6]


			# print(track_name) 
			# print(sample_name)
			# print('-' * 5)

		list_item = {
			'sample_url': url,
			'track_artist': track_artist,
			'track_name': track_name,
			'sampled_artist': sampled_artist,
			'sample_name': sample_name
		}

		all_items.append(list_item)

	with open('sample_data.json', 'w') as outfile:
		json.dump(all_items,outfile,indent=2)


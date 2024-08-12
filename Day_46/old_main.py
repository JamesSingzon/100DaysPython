from bs4 import BeautifulSoup 
import requests
from credentials import CLIENT_ID, CLIENT_SECRET
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import pprint

##Scope needed to create private playlist on Spotify
scope = "playlist-modify-private"

#Spotify URI Query
sp1 = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, scope=scope, redirect_uri="https://example.com"))
single_song_query = sp1.search(q="track:OMG year:2010")
print("""
      
      
      """)
query = single_song_query['tracks']['items'][0]['artists'][0]
pprint.pprint(query)
song_name = single_song_query['tracks']['items'][0]['artists'][0]['name']
song_id = single_song_query['tracks']['items'][0]['artists'][0]['id']
song_uri = single_song_query['tracks']['items'][0]['artists'][0]['uri']
print("""
      
      
      """)


##User ID query
# sp1 = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="https://example.com"))
# print(sp1.me()['id'])
# print(sp1.me()['display_name'])
ID = sp1.me()['id']
print(ID)
print("""
      
      
      """)

pprint.pprint(sp1.user_playlists(user=ID))

# # Create a user playlist
# sp1.user_playlist_create(user=ID, public=False, name="High School Playlist")

# # Add items to playlist
# uri_list = []
# uri_list.append(single_song_query['tracks']['items'][0]['artists'][0]['uri'])
# print(uri_list)

# sp1.playlist_add_items(playlist_id=, items=)









##Billboard Hot 100 for specified year
# from bs4 import BeautifulSoup
# import requests

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

# soup = BeautifulSoup(response.text, 'html.parser')
# song_names_spans = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_names_spans]

# print(song_names)

# time = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# time = "2010-05-10"

# response = requests.get(f"https://www.billboard.com/charts/hot-100/{time}")

# top_100_html = response.text

# soup = BeautifulSoup(top_100_html, "html.parser")

# My initial way of finding the first song
# song_title = soup.find(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet")
# print(song_titles)
#
# Using selectors to find song titles
# *Remember, selecting using an ID requires a pound sign and a class requires a period in between the quotation marks
# Selector parameter is by default in the first position and does not require selector= to be written out
# song_titles = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_titles]
# print(song_names[32])
# results = sp.search(q=f'track:{song_names[32]}, year:2010', type='artist')
# print(results)


##############
# >>> ID = sp1.me()['id']
# >>> sp1.user_playlists(user=ID)
# >>> playlists_dict = sp1.user_playlists(user=ID)
# >>> playlists_dict['total']
# >>> playlists_dict['items']
# >>> pprint.pprint(playlists_dict['items'])
# >>> sp1.user_playlist_create(user=ID, name="High School Playlist")
# >>> sp1 = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_T_SECRET,scope="playlist-modify-private", redirect_uri="https://example.com"))
# >>> sp1.user_playlist_create(user=ID, public=False, name="High School Playlist")
from bs4 import BeautifulSoup 
import requests
from credentials import CLIENT_ID, CLIENT_SECRET
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import pprint

# Billboard Hot 100 for specified year
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# test_date = "2010-05-10"
# test_response = requests.get(f"https://www.billboard.com/charts/hot-100/{test_date}")
# top_100_html = test_response.text
# soup = BeautifulSoup(top_100_html, "html.parser")
# song_names_spans = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_names_spans]

# Spotipy authorization
scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, scope=scope, redirect_uri="https://example.com"))

#User ID query
ID = sp.me()['id']

# Create a user playlist
playlist_id = sp.user_playlist_create(user=ID, public=False, name=f"{date} Billboard 100")['id']

# #Spotify URI Query
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        print(uri)
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Add items to playlist
sp.user_playlist_add_tracks(user=ID, playlist_id=playlist_id, tracks=song_uris)


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

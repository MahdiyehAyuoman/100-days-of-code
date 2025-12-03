import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# date_input = input('Which year do you want to travel to? Type the date in YYYY-MM-DD: ')

URL = "https://www.billboard.com/charts/hot-100/"

# Write your code below this line 
response = requests.get(URL)
music_website = response.text
# print(music_website)


soup = BeautifulSoup(music_website, 'html.parser')
## Get All 100 Top Music Title
all_musics = soup.select("li ul li h3")
all_musics_title = [song.getText().strip() for song in all_musics]
# print(all_musics_title)


clinet_id = 'd6d4aadebda2467ea97e27bbef44b19c'
client_secret = 'a76f40bd85964308a3beb9f176000ab4'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clinet_id,
                                               client_secret=client_secret,
                                               redirect_uri="https://open.spotify.com/",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username='Mahdiyehayuoman'))


user_id = sp.current_user()["id"]
print(user_id)


# Searching Spotify for songs by title
song_uris = []
# year = date.split("-")[0]
for song in all_musics_title:
    result = sp.search(q=f"track:{song}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


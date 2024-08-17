import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-private"

def find_song_names(html: BeautifulSoup) -> list:
    html_list = html.select("li ul li h3")
    song_names = [title.text.strip() for title in html_list]
    return song_names

page = requests.get("https://www.billboard.com/charts/hot-100/2023-07-22/")

page_html = BeautifulSoup(page.content, "html.parser")
song_names = find_song_names(page_html)
year = 2023
song_uris = []
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scope,
    redirect_uri="http://example.com",
    client_id="2d6c1e9c81034048a07c598fbf2e1a01",
    client_secret="70205d32ab814ae1b8911f027abbe7b3"))
results = sp.current_user()['id']
print(results)

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import os
from datetime import date

# Set up
scope = "playlist-modify-public user-top-read"
username = os.getenv("SPOTIFY_USERNAME")
token = SpotifyOAuth(scope = scope, username = username)
spotify = spotipy.Spotify(auth_manager = token)

# Create playlist
playlist_name = date.today().strftime("%b %y").lower()
playlist_description = "monthly playlist for " + date.today().strftime("%B %Y").lower() + " automatically generated using the spotify web api"
spotify.user_playlist_create(username, playlist_name, public = True, description = playlist_description)

# Populate playlist
limit = 10
tracks = spotify.current_user_top_tracks(limit = limit, offset = 0, time_range = "short_term")

all_playlists = spotify.user_playlists(user=username)
playlist_id = all_playlists["items"][0]["id"]

track_list = []
for track in tracks['items']:
    track_list.append(track['uri'])

spotify.user_playlist_add_tracks(user=username, playlist_id=playlist_id, tracks=track_list)

print(f"Playlist \"{playlist_name}\" created!")

#Create a playlist with random tracks from your saved tracks collection in Spotify.
###This is a python script, if you want to make your own random playlist here are the requirements and steps to follow:
Requirements:
- Spotify Account
- Python 3.x
Steps-to-follow:
1.- First at all, you need to download the 'test.py' file. 
2.- You have to create a playlist in Spotify with at least one track inside and then obtain their playlist_id (you can obtain it by copying the URI (i.e: spotify:user:user_id:playlist:playlist_id)).
3.- Then using pip you have to install spotipy. Like this:
"pip install spotipy"
4.- For setting up spotipy you can do it using this https://spotipy.readthedocs.io/en/latest
5.- If you have your app on spotify and you have installed spotipy succesfully now you only have to fill the information that 'test.py' needs.
6.- Finally, after you fill it, you can create your random playlist by running:
"python test.py user_id"
**If it is the first time you run the script, it will ask you for a token (everything is explained in spotipy's documentation, so just check it out)**
Just wait some minutes and that's all. Now you have your playlist ready !
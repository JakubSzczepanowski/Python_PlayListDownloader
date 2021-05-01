import pytube
url = input('Wpisz url playlisty: ')
yt = pytube.Playlist(url)
for y in yt.videos:
    y.streams.get_audio_only().download()
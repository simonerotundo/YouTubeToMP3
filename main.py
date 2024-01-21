from VideoHandler import VideoHandler
from PlaylistHandler import PlaylistHandler

def is_a_video(url):
    if url.__contains__("watch"):
        return True
    return False

def is_a_playlist(url):
    if url.__contains__("playlist"):
        return True
    return False

# definisco un path in cui salvare i file
path = "/Users/simonerotundo/Downloads/YouTubeDownloader"

# richiedo in input un URL ad un video o ad una playlist di YouTube
url ="https://www.youtube.com/playlist?list=PLHyR7AeDqEe60okBbejnikJvesmSO4U9K"# input("inserisci URL di YouTube (Video/Playlist)\n-> ")

# se il link inserito corrisponde ad un video, lo gestisco come singolo video
if is_a_video(url):
    video_url = url
    VideoHandler(video_url, path)

# altrimenti, se il link inserito corrisponde ad una playlist, lo gestisco come insieme di video
elif is_a_playlist(url):
    playlist_url = url
    PlaylistHandler(playlist_url, path)
    
# altrimenti, probabilmente il link non appartiene a youtube
else:
    print("???")

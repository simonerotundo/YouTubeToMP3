from pytube import YouTube
from pytube import Playlist
import os


class PlaylistHandler:

    def __init__(self, url, path_to_save):

        # Ottieni il link della playlist da input
        playlist_url = url

        # Estrai i link dei video dalla playlist
        video_links = self.extract_video_links(playlist_url)

        # Itera attraverso i video e chiama la funzione info per ciascuno
        for video_link in video_links:
            VideoHandler(video_link,path)

    def extract_video_links(self, playlist_url):
        playlist = Playlist(playlist_url)
        video_links = playlist.video_urls
        return video_links


class VideoHandler:

    def __init__(self, url, path_to_save):

        # Stampo lo stato dell'esecuzione
        print("Running..")

        # Ottenere l'URL del video da scaricare dall'utente
        video_url = url
        yt = YouTube(video_url)

        # Selezionare la prima traccia audio disponibile
        audio = yt.streams.get_highest_resolution() or yt.streams.filter(only_audio=True).first()

        # Stampare il titolo del video
        print("title: ", audio.title)

        # Definire la destinazione del file scaricato
        destination = path_to_save

        # Scaricare il file audio
        audio.download(destination)

        # Stampo l'esito
        print(yt.title + " has been successfully downloaded in .mp3 format.")


class MP4ToMP3Converter:

    def __init__(self, path):
        # Elencare tutti i file nella directory specificata
        files = os.listdir(path)
        ext_old = ".mp4"
        ext_new = ".mp3"

        # Iterare attraverso i file e rinominare quelli che contengono la vecchia sottostringa
        for file_name in files:
            if ext_old in file_name:
                # Costruire il nuovo nome del file sostituendo la vecchia sottostringa con la nuova
                new_file_name = file_name.replace(ext_old, ext_new)

                # Costruire i percorsi completi dei file vecchio e nuovo
                old_file_path = os.path.join(path, file_name)
                new_file_path = os.path.join(path, new_file_name)

                # Rinominare il file
                os.rename(old_file_path, new_file_path)



path = "."
url = input("inserisci URL di YouTube (Video/Playlist)\n-> ")
if url.__contains__("watch"):
    VideoHandler(url, path)
elif url.__contains__("playlist"):
    PlaylistHandler(url, path)
else:
    print("???")

MP4ToMP3Converter(path)

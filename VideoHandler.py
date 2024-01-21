from pytube import YouTube
from threading import Thread


class VideoHandler:

    def __init__(self, url, path_to_save):
        self.video_url = url                # url del video
        self.path_to_save = path_to_save    # path in cui salvare il video
        
        # oggetto del video
        self.yt = YouTube(self.video_url)

        # cerco e scarico il video
        self._search_and_download()


    def _search_and_download(self):

        # seleziono la qualità massima (se disponibile), altrimenti la prima che trovo
        audio = self.yt.streams.get_highest_resolution() or self.yt.streams.filter(only_audio=True).first()

        # stampo il titolo del video
        print("Title: ", audio.title)

        # scarico il video e lo inserisco nel path indicato
        audio.download(self.path_to_save)

        # stampo l'esito
        print(self.yt.title + " has been successfully downloaded in .mp3 format.")


class VideoHandlerThread(Thread):

    def __init__(self, url, path_to_save):
        super().__init__()
        self.url = url
        self.path_to_save = path_to_save

    def run(self):
        VideoHandler(self.url, self.path_to_save)   

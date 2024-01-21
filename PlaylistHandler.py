from VideoHandler import VideoHandlerThread
from ExtensionHandler import ExtensionHandlerThread
from pytube import Playlist
import os


class PlaylistHandler:

    def __init__(self, url, path_to_save):
        self.playlist_url = url                                         # url della playlist
        self.playlist_title = Playlist(url).title                       # titolo della playlist
        self.path_to_save = path_to_save                                # path in cui salvare il video
        self.video_links = self._extract_video_links(self.playlist_url) # link a tutti i video presenti nella playlist

        # scarico tutti i video presenti nella playlist
        self._update_path()
        self._download_video()


    def _extract_video_links(self, playlist_url):
        playlist = Playlist(playlist_url)
        video_links = playlist.video_urls
        return video_links

    def _update_path(self):
        self.path_to_save += f"/{self.playlist_title}"

    def _download_video(self):
        # deve attivare i thread, e restare in attesa che finiscano
        thread_pool = []
        for video_url in self.video_links:
            thread = VideoHandlerThread(video_url, self.path_to_save)
            thread_pool.append(thread)
            thread.start()

        for thread in thread_pool:
            thread.join()

        self._convert_video()
        
    def _convert_video(self):
        # deve attivare i thread, e restare in attesa che finiscano
        thread_pool = []
        for file_name in os.listdir(self.path_to_save):
            file_path = os.path.join(self.path_to_save, file_name)

            # Check if the item is a file (not a directory) and has the .mp4 extension
            if os.path.isfile(file_path) and file_name.lower().endswith(".mp4"):
                thread = ExtensionHandlerThread(file_path)
                thread_pool.append(thread)
                thread.start()

        # Wait for all threads to finish
        for thread in thread_pool:
            thread.join()

    def get_playlist_title(self):
        return self.playlist_title
    
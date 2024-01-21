from os import path
from subprocess import CalledProcessError, run
from threading import Thread


class ExtensionHandler:

    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        self._mp4_to_m4a()

    def _mp4_to_m4a(self):
        # verifico che il path esista
        if not path.exists(self.path_to_file):
            print(f"Il percorso '{self.path_to_file}' non esiste.")
            return

        # se il path corrisponde ad un file con estensione .mp4, lo converto in .m4a
        if path.isfile(self.path_to_file) and self.path_to_file.lower().endswith(".mp4"):
            # sostituisco l'estensione mp4 con l'estensione .m4a
            nuovo_nome = path.splitext(path.basename(self.path_to_file))[0] + ".m4a"
            nuovo_percorso = path.join(path.dirname(self.path_to_file), nuovo_nome)

            # converto il file in .m4a
            comando = ["ffmpeg", "-i", self.path_to_file, nuovo_percorso]
            try:
                run(comando, check=True)
            except CalledProcessError as e:
                print("Exception in ExtensionHandler")

            # Rimuove il file .mp4 dopo la conversione
            path_to_remove = self.path_to_file
            if path.isfile(path_to_remove) and path_to_remove.lower().endswith(".mp4"):
                remove(path_to_remove)

        
class ExtensionHandlerThread(Thread):

    def __init__(self, path):
        super().__init__()
        self.path = path

    def run(self):
        ExtensionHandler(self.path)

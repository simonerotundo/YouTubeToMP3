How to run:
- pip install -r requirements
- run main.py
- insert a link redirecting to a YouTube's video or playlist
- wait for the download and the conversion to finish

###

i just updated the script, so it now converts the result to ".a4m". you can avoid that by removing the call to the class ExtensionHandler/ExtensionHandlerThread in the PlaylistHandler class. You will get an .mp4 for every song in the playlist, and at this point you can just rename it as ".mp3" and it will do the job. i will make everything more intuitive in a few days :)

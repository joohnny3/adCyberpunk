import os
import certifi
from pytube import YouTube

os.environ['SSL_CERT_FILE'] = certifi.where()

# YouTube('https://www.youtube.com/watch?v=L7_gadHPA1k').streams.first().download()
yt = YouTube('https://www.youtube.com/watch?v=L7_gadHPA1k')

(yt.streams
   .filter(progressive=True, file_extension='mp4')
   .order_by('resolution')
   .desc()
   .first()
   .download())

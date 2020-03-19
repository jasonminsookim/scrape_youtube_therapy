# Import libraries
import youtube_dl
import pandas as pd

# Import the youtube urls to scrape the audio from.
urls = pd.read_csv('../data/youtube_urls/therapy_youtube_urls.csv')

# Set the youtube download options.
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])
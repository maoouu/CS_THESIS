# youtube_converter.py

import os
import pytube
from config import UPLOAD_FOLDER

def create_uploads_folder():
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)


def download_youtube_audio(link):
    create_uploads_folder()  # Create the /uploads folder if it doesn't exist
    # Download YouTube audio as .mp4 file
    video = pytube.YouTube(link)
    stream = video.streams.filter(only_audio=True).first()
    audio_file = os.path.join(UPLOAD_FOLDER, stream.download())
    return audio_file


def get_title(link):
    return pytube.YouTube(link).title

# youtube_converter.py

import os
import pytube
import librosa
import numpy as np
from pydub import AudioSegment
from features import extract_features
from model import KNeighborsClassifierModel

UPLOADS_FOLDER = 'uploads'  # Set the path to your /uploads folder

def create_uploads_folder():
    if not os.path.exists(UPLOADS_FOLDER):
        os.makedirs(UPLOADS_FOLDER)

def download_youtube_audio(link):
    create_uploads_folder()  # Create the /uploads folder if it doesn't exist
    # Download YouTube audio as .mp4 file
    video = pytube.YouTube(link)
    stream = video.streams.filter(only_audio=True).first()
    audio_file = os.path.join(UPLOADS_FOLDER, stream.download())
    return audio_file

def convert_to_wav(input_file):
    create_uploads_folder()  # Create the /uploads folder if it doesn't exist
    # Convert downloaded audio to .wav format using ffmpeg
    mp3_filename = input_file
    wav_filename = os.path.join(UPLOADS_FOLDER, os.path.splitext(os.path.basename(mp3_filename))[0] + '.wav')
    os.system(f'ffmpeg -i "{mp3_filename}" -acodec pcm_s16le -ar 22050 "{wav_filename}"')
    return wav_filename

def classify_youtube_audio(audio_file):
    model = KNeighborsClassifierModel()
    audio, sample_rate = librosa.load(audio_file, sr=None)
    features = extract_features(audio, sample_rate)
    features_df = pd.DataFrame([features])
    genre = model.predict(features_df)

    # Clean up by removing the .mp4 file
    os.remove(audio_file)

    return genre[0]
